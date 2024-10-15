import time
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from implementations import all_implementations

start_total = time.time()

data = []

for _ in range(45):
    random_array = np.random.randint(low=-10000, high=10000, size=10000)
    for sort in all_implementations: ##############Increse to right size based on CSIL
        st = time.time()
        res = sort(random_array)
        en = time.time()
        runtime = en - st
        data.append([sort.__name__, runtime])


df = pd.DataFrame(data, columns=['Algorithm', 'Runtime'])
df.to_csv('data.csv', index=False)

end_total = time.time()

print("Total Runtime: " + str(end_total - start_total) + " Seconds\n")

print(df)

# Plotting the results
# plotting a scatter plot 
plt.scatter(df["Algorithm"], df["Runtime"]) 
plt.show() 

