import matplotlib.pyplot as plt
import numpy as np
students = ["AMIT","RIYA","JOHN"]
marks = [85,92,78]
plt.figure(figsize = (7,5))
plt.bar(students , marks)
plt.title("student performance dashboard")
plt.xlabel("students")
plt.ylabel("marks")
for i in range(len(students)):
    plt.text(i,marks[i] + 1,str(marks[i]),ha = 'center')
plt.show()
maths = [85,92,78]
science = [88,90,80]
x = np.arange(len(students))
width = 0.35
plt.figure(figsize = (8,5))
plt.bar(x- width/2,maths ,width,label = "maths")
plt.bar(x + width/2,science,width,label = "science")
plt.xticks(x, students)
plt.title("student performance comparison")
plt.xlabel("students")
plt.ylabel("marks")
plt.legend()
plt.show
