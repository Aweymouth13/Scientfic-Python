import pandas as pd
import matplotlib.pyplot as plt

def kaprekar_routine(n):
    count = 0
    while n != 6174:
        str_n = str(n).zfill(4)
        asc = ''.join(sorted(str_n))
        desc = ''.join(sorted(str_n, reverse=True))
        n = int(desc) - int(asc)
        count += 1
    return count

# create empty DataFrame
df = pd.DataFrame(columns=['Number', 'Iterations'])

# iterate through 4-digit numbers
for i in range(1000, 10000):
    if len(set(str(i))) > 1:
        iterations = kaprekar_routine(i)
        df = df.append({'Number': i, 'Iterations': iterations}, ignore_index=True)

# create histogram
plt.hist(df['Iterations'], bins=range(0, df['Iterations'].max() + 1), align='left', alpha=0.7)
plt.xlabel('Iterations')
plt.ylabel('Frequency')
plt.title('Kaprekar Routine Iterations')
plt.show()
