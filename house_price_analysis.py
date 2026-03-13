import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("train.csv")

print("\nFirst 5 rows of dataset:\n")
print(df.head())

print("\nDataset Information:\n")
print(df.info())

print("\nSummary Statistics:\n")
print(df.describe())

plt.figure()
sns.scatterplot(x="GrLivArea", y="SalePrice", data=df)

plt.title("Living Area vs House Price")
plt.xlabel("Living Area (sq ft)")
plt.ylabel("Sale Price")

plt.show()

plt.figure(figsize=(10,6))
sns.heatmap(df[["SalePrice","GrLivArea","OverallQual","GarageCars"]].corr(),
            annot=True)

plt.title("Correlation Heatmap")

plt.show()