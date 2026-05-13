import pandas as pd
data = {
    "NAME" : ["A","B" ,"C","D"],
    "DEPT" : ["IT","HR","IT","HR"],
    "SALARY" :[50000,40000,60000,45000]
}
df = pd.DataFrame(data)
print("employee data:",df)
avg_salary = df.groupby("DEPT")["SALARY"].mean()
print("\n Average salary per department :\n",avg_salary)
highest_paid = df.loc[df.groupby("DEPT")["SALARY"].idxmax()]
print("\n highest paid employee per department:\n",highest_paid)
employee_count = df.groupby("DEPT")["NAME"].count()
print("\n employee count per department:\n",employee_count)
sorted_avg_salary = avg_salary.sort_values(ascending= False)
print("\ndepartment sorted by average:\n",sorted_avg_salary)