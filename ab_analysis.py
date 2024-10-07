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




#####CONTINUE AFTER LECTURE


def main():
    searchdata_file = sys.argv[1]

    df = pd.read_json(searchdata_file, orient='records', lines=True)

    df['searched'] = df['search_count'] > 0
    df['group'] = np.where(df['uid'] % 2 == 0, 'even', 'odd') 

    


    # # Output
    # print(OUTPUT_TEMPLATE.format(
    #     more_users_p=0,
    #     more_searches_p=0,
    #     more_instr_p=0,
    #     more_instr_searches_p=0,
    # ))


if __name__ == '__main__':
    main()