import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os



# create a dictionary of series

d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack', 'Lee',
                        'Chanchal', 'Gasper', 'Naviya', 'Andres']),
     'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])}

# create a DataFrame
df = pd.DataFrame(d)
print(df)
print("Mean Values in the Distribution")
print(df[['Age', 'Rating']].mean())

print("Median Values in the Distribution")
print(df[['Age', 'Rating']].median())

print("Mode Values in the Distribution")
print(df[['Age', 'Rating']].mode())

# Calculate the standard deviation

print("Standard Deviation")
print(df[['Age', 'Rating']].std())

# Measuring Skewness

print("Skewness")
print(df[['Age', 'Rating']].skew())

# Normal Distribution

mu, sigma = 0.5, 0.1
s = np.random.normal(mu, sigma, 1000)

# Create the bins and histogram
count, bins, ignored = plt.hist(s, 20, density=True)

# Plot the distribution curve
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
         np.exp(- (bins - mu) **2 / (2 * sigma**2) ),linewidth=3,
                color='y')
plt.show()


# Correlation

df_iris = sns.load_dataset('iris')

# Without regression
sns.pairplot(df_iris, kind="scatter")
plt.show()

# CSV
file_path = os.path.expanduser("~/Downloads/data(1).csv")
df_corr = pd.read_csv(file_path)
print(df_corr.head)
#print(df_corr.corr())
