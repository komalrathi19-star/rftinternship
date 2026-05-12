import pandas as pd
data = {
    "NAME" :["AMIT","RIYA","JOHN"],
    "MATH" :[80,90,60],
    "SCIENCE" :[70,88,65],
    "ENGLISH" :[85,92,70]
}
df = pd.DataFrame(data)
df["AVERAGE"] = (df["MATH"] + df["SCIENCE"] + df["ENGLISH"]) / 3
topper = df.loc[df["AVERAGE"].idxmax()]
overall_avg = df["AVERAGE"].mean()
above_avg_count = (df["AVERAGE"] > overall_avg).sum()
def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >=75:
        return "A"
    elif avg >= 60:
        return "B"
    else:
        return "C"
df["GRADE"] = df["AVERAGE"].apply(grade)
subject_avg = df[["MATH","SCIENCE","ENGLISH"]].mean()
print("student performance dashboard \n")
print(df)
print("\nTooper:")
print(topper["NAME"],"-",topper["AVERAGE"])
print("\n oerall average:",overall_avg)
print("\n students above average:",above_avg_count)
print("\nsubject -wise average:")
print(subject_avg)