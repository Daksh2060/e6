import sys
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency, mannwhitneyu

OUTPUT_TEMPLATE = (
    '"Did more/less users use the search feature?" p-value:  {more_users_p:.3g}\n'
    '"Did users search more/less?" p-value:  {more_searches_p:.3g} \n'
    '"Did more/less instructors use the search feature?" p-value:  {more_instr_p:.3g}\n'
    '"Did instructors search more/less?" p-value:  {more_instr_searches_p:.3g}'
)


def more_users_p_value(control, treatment):
    
    control_search_count = (control['search_count'] > 0).sum()
    control_not_search_count = (control['search_count'] <= 0).sum()
    
    treatment_search_count = (treatment['search_count'] > 0).sum()
    treatment_not_search_count = (treatment['search_count'] <= 0).sum()

    #Format of contigency table adapted from: https://pythonfordatascienceorg.wordpress.com/chi-square-python/
    table = [[control_search_count, control_not_search_count],
             [treatment_search_count, treatment_not_search_count]]
    
    _, pvalue, _, _ = chi2_contingency(table, correction=False)
    return pvalue


def more_searches_p_value(control, treatment):
    _, pvalue = mannwhitneyu(control['search_count'], treatment['search_count'], alternative='two-sided')
    return pvalue


def main():
    searchdata_file = sys.argv[1]

    df = pd.read_json(searchdata_file, orient='records', lines=True)

    print(df[df["is_instructor"]].count())

    even = df[df['uid'] % 2 == 0]
    odd = df[df['uid'] % 2 != 0]
    
    even_instructor = even[even['is_instructor']]
    odd_instructor = odd[odd['is_instructor']]

    

    print(OUTPUT_TEMPLATE.format(
        more_users_p = more_users_p_value(even, odd),
        more_searches_p = more_searches_p_value(even, odd),
        more_instr_p = more_users_p_value(even_instructor, odd_instructor),
        more_instr_searches_p = more_searches_p_value(even_instructor, odd_instructor)
    ))


if __name__ == '__main__':
    main()