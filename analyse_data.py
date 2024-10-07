import pandas as pd
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd

data = pd.read_csv('data.csv')

# adapted from https://www.statology.org/tukey-test-python/
melted_data = data.melt(id_vars='Algorithm', value_vars='Runtime', var_name='Metric', value_name='Time')
tukey_results = pairwise_tukeyhsd(endog=melted_data['Time'], groups=melted_data['Algorithm'], alpha=0.05)

print(tukey_results)

# negative meandiff means difference in mean runtime between the two groups (group1 - group2). A negative value indicates that group1 is faster than group2.
# reject indicates whether to reject the null hypothesis. If True, it means there is a statistically significant difference between the means of the two groups.


