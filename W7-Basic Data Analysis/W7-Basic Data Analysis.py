import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv('Iris-(1).csv')

##Check dataframe
print(df.head())

print(df.dtypes)

print(df.isnull().sum())

print(df.columns)

print(df.shape)

print(df.info())

result1 = df.groupby('Species')['SepalLengthCm'].agg(['mean'])

result2 = df.groupby('Species')['SepalWidthCm'].agg(['mean'])

result3 = df.groupby('Species')['PetalLengthCm'].agg(['mean'])

result4 = df.groupby('Species')['PetalWidthCm'].agg(['mean'])

##Line plot for Sepal Length
result1 = result1.reset_index()
plt.figure(figsize=(8, 6))
sns.lineplot(data=result1, x='Species', y='mean', marker='o', color='orange')
plt.xlabel('Species')
plt.ylabel('Average Sepal Length (cm)')
plt.title('Average Sepal Length by Species')
plt.show()

##Bar plot for Sepal Width
plt.figure(figsize=(8, 6))
plt.bar(result2.index, result2['mean'], color='b')
plt.xlabel('Species')
plt.ylabel('Average Sepal Width (cm)')
plt.title('Average Sepal Width by Species')
plt.show()

##Pie chart for Petal Length
plt.figure(figsize=(8, 6))
plt.pie(result3['mean'], labels=result1.index, autopct='%1.1f%%', startangle=90)
plt.title('Average Petal Length (cm) Distribution by Species')
plt.show()

##Histogram for Petal Width
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='SepalLengthCm', hue='Species', bins=20, kde=False, element='step', stat='count', palette='deep')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Frequency')
plt.title('Distribution of Petal Width among Species')
plt.show()




