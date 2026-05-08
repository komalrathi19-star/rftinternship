# basic CSV reader without pandas
data = []
with open("students.csv","r")as file:
    # read all lines
    lines = file.readlines()
    # get headings
    headers = lines[0].strip().split(",")
    #read data rows
    for line in lines[1:]:
        values = line.strip().split(",")
        # handle missing values
        if len(values) < len(headers):
            continue
        student = {
            "NAME": values[0],
            "AGE":int(values[1]),
            "MARKS": int(values[2])
        }
        data.append(student)
# print data
print(data)
# calculate average marks
total = 0
for student in data:
    total +=student["MARKS"]
average = total / len(data)
print("Average Marks:",average)