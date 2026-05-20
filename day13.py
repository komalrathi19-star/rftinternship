import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
marks = [45,56,67,78,89,90,76,65,54,43,88,92,74,69,58,81,73,64,58,47]
df= pd.DataFrame({"Marks": marks})
print(df.head())
plt.figure(figsize = (8,5))
sns.histplot(df["Marks"],bins = 8,kde = True,color = "skyblue")
plt.title("distribution o student marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
skewness = df["Marks"].skew()
print("skewness of data:",skewness)
if skewness > 0:
    print("the distribution is positively skewed")
elif skewness < 0:
    print("the distribution is negatively skewed")
else:
    print("the distribution is symmetrical")