import time
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from implementations import all_implementations

start_total = time.time()

data = []
random_array = np.random.randint(low=-10000, high=10000, size=10000)

for sort in all_implementations:
    for _ in range(20): ##############Increse to right size based on CSIL
        st = time.time()
        res = sort(random_array)
        en = time.time()
        runtime = en - st
        data.append([sort.__name__, runtime])


df = pd.DataFrame(data, columns=['Algorithm', 'Execution_Time'])
df.to_csv('data.csv', index=False)

end_total = time.time()

print("Total Runtime: " + str(end_total - start_total) + " Seconds\n")

print(df)

# Plotting the results
# plotting a scatter plot 
plt.scatter(df["Algorithm"], df["Execution_Time"]) 
plt.show() 

