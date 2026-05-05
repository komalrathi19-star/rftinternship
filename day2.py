marks = [78,85,90,67,85,92,78]
avg = sum(marks) / len(marks)
# highest & lowest
highest = max(marks)
lowest = min(marks)

# count above average
above_avg = 0
for m in marks:
    if m > avg:
        above_avg += 1

grades = {"A": 0,"B ": 0,"C": 0,"Fail": 0}
for m in marks:
    if m >= 90:
        grades["A"] += 1
    elif m >= 80:
        grades["B "] += 1
    elif m >= 70:
        grades["C"] += 1
    else:
        grades["Fail"] += 1

# output
print("average:", round(avg,2))
print("highest :",highest)
print("lowest",lowest)
print("students above average:",above_avg)
print("grade distribution :",grades)