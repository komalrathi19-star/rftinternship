# day1
# Description
This Python program removes duplicate values and invalid entries like None and empty strings from a list and returns a clean list.
# Features
Removes duplicates
Removes invalid values
Counts removed elements
## Example
Input: [10, None, 20, 10, "", 30, None, 40]
Output: [10, 20, 30, 40]
Removed values: 4
# Run
python day1.py

# day 2
# Description 
This python program calculate average , highest , lowest , count how many student score above average and create grade distribution for them
# Features 
calculate average calculate highest & lowest count students scored above average create grade distribution
## Example
Input : [78,85,90,67,85,92,78] 
Output :average: 82.14
highest : 92
lowest 67
students above average: 4
grade distribution : {'A': 2, 'B ': 2, 'C': 2, 'Fail': 1}
# Run 
python day2.py
# day 3
# Description
This project is a menu - driven phonebook application developed in python using dictionaries .It allows users to manage contacts with features like adding , searching , deleting and displaying contacts.
# Features
Add new contact
Search contact
Delete contact
Display all contacts
prevent duplicate entries
Menu - driven interface
## Example
Input : --- PHONEBOOK MENU ---
1. Add Contact
2. Search Contact
3. Delete Contact
4. Display All Contacts
5. Exit

Enter your choice: 1
Enter name: Rahul
Enter phone number: 9356648234
Output: Contact added successfully!
Enter your choice: 2
Enter name to search: AMIT
AMIT: 9876543210
Enter your choice: 3
Enter name to delete: RIYA
Output: Contact deleted successfully!
Input: Enter your choice: 4

Output: Phonebook Contacts:
AMIT : 9876543210
RAHUL : 9988776655
Input: Enter your choice: 5
Output: Exiting program...
# Run
python day3.py

# day 4
# Description
A basic Python project that analyzes system log messages and counts different log types like ERROR, INFO, and WARNING. It also finds the most frequent log type while ignoring case sensitivity.
# Features
Count ERROR logs
Count INFO logs
Count WARNING logs
Find the most frequent log type
Ignore case sensitivity using string processing
##  Example
Input : logs = [
    "ERROR DISK FULL",
    "INFO STARTED",
    "ERROR FILE MISSING",
    "WARNING MEMORY LOW"
]
Output:
ERROR Count: 2
INFO Count: 1
WARNING Count: 1
Most Frequent Log Type: ERROR
# Run
python day4.py
# day 5
# Description:
A simple Python program to read and process CSV files without using the Pandas library.
# Features:
Reads CSV file data
Stores data in list of dictionaries
Uses file handling and string splitting
Beginner-friendly Python project
# Run 
python day5.py
# day 6
# Description
A simple Python project that analyzes sales data using the Pandas library.
This project reads data from a CSV file, performs aggregation, and generates useful sales insights.
# Features
Read data from CSV file
Add a new TOTAL column (QUANTITY × PRICE)
Calculate total sales per product
Find total revenue
Identify top-selling product
Sort products by revenue
Technologies Used
Python
Pandas
# Run 
python day6.py
# day 7
# Description
A simple Python project using Pandas to analyze student marks and generate a performance dashboard.
# Features
Create and manage student data using DataFrame
Calculate average marks of each student
Find the topper of the class
Count students scoring above overall average
Add grade column based on performance
Calculate subject-wise average marks
🛠️ Technologies Used
Python
Pandas
# Run
python day7.py
