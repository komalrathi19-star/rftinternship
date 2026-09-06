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
# day 8
# Description
This project analyzes employee salary data using Python and Pandas.
It demonstrates the use of Grouping and Aggregation (groupby) operations for data analysis.
# Features
Find average salary per department
Find highest paid employee in each department
Count employees department-wise
Sort departments based on average salary
🛠️ Technologies Used
Python
Pandas
# Run
python day8.py
# day 9
# Description
This project is a simple Data Filtering Tool built using Python and Pandas.
It demonstrates how to filter data from a dataset using multiple conditions.
The program filters employees whose:
Salary is greater than 50000
Age is less than 30
Filtered results are displayed and also saved into a new CSV file.
# Features
Create and manage dataset using Pandas
Apply Boolean Filtering
Use multiple conditions together
Display filtered records
Save filtered data into a new CSV file
🛠️ Technologies Used
Python
Pandas
# day 10
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
python day10.py
# day 11
# Description
This project is a simple Sales Trend Visualization created using Python and Matplotlib.
It displays daily sales data using a line chart and highlights the highest and lowest sales days.
# Features
Line plot using Matplotlib
Time-series sales visualization
Highlights highest and lowest sales
Added labels, title, and grid
Simple trend analysis
# Technologies Used
Python
Matplotlib
# Run
python day11.py
# day 12
# Description
# Student Performance Dashboard 📊

A simple Python project to visualize student marks using bar charts and grouped bar charts with Matplotlib.

# 🚀 Features
- Simple Bar Chart of student marks
- Comparative Visualization
- Grouped Bar Chart for multiple subjects
- Marks displayed on bars

# 🛠️ Technologies Used
- Python
- Matplotlib
- NumPy

# Run
python day12.py
# day 13
# Description
📌 Project Overview
This project performs Distribution Analysis using Python and Seaborn.
It visualizes student marks data with a Histogram and KDE Curve to understand data distribution and identify skewness.
# 🚀 Features
Histogram Visualization
KDE (Kernel Density Estimation) Curve
Distribution Understanding
Skewness Identification
# 🛠 Technologies Used
Python
Pandas
Matplotlib
Seaborn
# day 14
# Description
This project visualizes expense distribution using a Pie Chart in Python.

# Concepts Used
- Pie Chart Visualization
- Percentage Labels
- Highlighting Highest Category

# Dataset
- Food: 500
- Travel: 300
- Shopping: 200

# Libraries Used
- Matplotlib
# Run
python day13.py
# day 15
# Description

This project is a Mini EDA Dashboard created using Python.

##Features
- Line Chart for Trend Analysis
- Bar Chart for Comparison
- Histogram for Distribution
- Insights Generation
- Subplots Visualization

# Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn
- # Run
- python day15.py
# day 16
# Description
This project performs Exploratory Data Analysis (EDA) on a sales dataset using Python.
The analysis includes data cleaning, aggregation, visualization, and business insight generation.
# Features
-Handle missing values
-Product-wise sales analysis
-Region-wise performance analysis
-Sales trend visualization
-Top product identification
-Monthly growth analysis
-Best performing region detection
## Technologies Used
-Python
-Pandas
-NumPy
-Matplotlib
-Seaborn
# Run 
python day16.py
# day 17
# Description
Customer Segmentation Analysis is a data analysis project that groups customers based on their spending behavior and visit frequency.
The project helps businesses identify high-value customers, low-engagement users, and create targeted marketing strategies.
# Features
Customer grouping based on spending levels
Identification of:
High-value customers
Low-engagement users
Spending distribution visualization
Customer category visualization
Business strategy suggestions
Simple segmentation (High / Medium / Low)
# Technologies Used
Python
Pandas
Matplotlib
# Run
python day17.py
# day 18
# Description
A simple Python data analysis project that explores movie ratings, genres, and revenues using Pandas and Matplotlib.
## 📌 Project Objective
This project analyzes a movie dataset to:
Find the highest rated movies
Identify the most profitable genres
Visualize movie trends
Understand the correlation between ratings and revenue
## 🛠 Technologies Used
Python
Pandas
Matplotlib
## 📂 Dataset Columns
The dataset contains:
Movie Name
Rating
Genre
Revenue
# ✨ Features
✅ Highest Rated Movies
Finds the movie with the maximum rating.
✅ Most Profitable Genres
Calculates total revenue generated by each genre.
✅ Top 5 Movies
Displays the top-rated movies.
✅ Correlation Analysis
Checks the relationship between:
Movie Rating
Revenue
# Run
python day18.py
#  day 19
# Description
This project performs Stock Market Time-Series Analysis using Python.
It analyzes stock prices over time, calculates moving averages, identifies peaks and drops, and visualizes stock trends using graphs.
The project helps understand:
Time-Series Analysis
Trend Detection
Moving Average
Volatility Detection
Data Visualization
## 🛠 Technologies Used
Python
Pandas
Matplotlib
# day 20
# Description
A complete Data Analysis and Visualization project built using Python, Pandas, and Matplotlib.
# 🚀 Features
✔ Cleaned and processed sales dataset
✔ Calculated total sales
✔ Analyzed sales region-wise
✔ Identified top-selling product category
✔ Created:

Pie Chart
Bar Chart
Dashboard-style visualization
# day 21

## description
This project focuses on using Python functions with *args, **kwargs, and return values.
## Tasks
Check whether a number is prime.
Find the largest number using *args.
Display student details using **kwargs.
Calculate maximum, minimum, average, and sum of numbers.
## Concepts Used
Functions
*args and **kwargs
Loops & conditions
max(), min(), sum(), len()
## How to run
python Day 21.py


✔ Generated business insights from data

# 📂 Technologies Used
Python
Pandas
Matplotlib
#day22
#📌 Description
A Python-based Sales & Customer Insights Dashboard that analyzes sales data from a CSV dataset. It cleans the data, calculates sales metrics, identifies top customers and products, and generates visual insights through charts.
##✨ Features
Data cleaning and duplicate removal
Missing-value handling
Total sales calculation
Average revenue calculation
Top 5 customers identification
Top 5 products analysis
Sales trend visualization
Category-wise sales distribution
5 business insights generation
##🛠️ Technologies
Python
Pandas – data cleaning and analysis
Matplotlib – data visualization
CSV – dataset format
#day23
##📌 Description
The Employee Performance Analytics System is a Python-based data analysis project that analyzes employee performance and attendance data using a CSV dataset.
The project calculates department-wise performance, identifies the top-performing employees, detects employees with attendance below 75%, generates visualizations, and exports the final report as a CSV file.
An interactive Streamlit dashboard is also included as a bonus feature.
##✨ Features
📥 Import employee data from CSV
🧹 Remove duplicate and missing records
📊 Calculate department-wise average performance
🏆 Identify Top 10 performers
⚠️ Find employees with attendance below 75%
📊 Generate Performance Comparison Chart
📈 Generate Attendance Trend
🥧 Generate Department Distribution chart
📁 Export final employee report as CSV
🎛️ Interactive department filter using Streamlit
📥 Download filtered data from the dashboard
#🛠️ Technologies Used
Python
Pandas – Data cleaning and analysis
Matplotlib – Data visualization
Streamlit – Interactive dashboard
CSV – Dataset and report format
#day24

##📌 Description

The Weather Data Analytics System is a Python-based project that analyzes weather information stored in a CSV file. It calculates temperature statistics, identifies the hottest and coldest cities, counts rainy and sunny days, generates visualizations, and exports the final analysis report.

The project also includes a Moving Average Prediction feature to estimate tomorrow's temperature and an optional Streamlit dashboard for interactive analysis.

##✨ Features

- 📂 Read weather data from a CSV file
- 🌡️ Calculate average temperature for each city
- 🔥 Identify the hottest city
- ❄️ Identify the coldest city
- 🌧️ Count rainy days
- ☀️ Count sunny days
- 📈 Generate temperature trend visualization
- 🌦️ Generate weather distribution chart
- 📊 Generate average temperature per city chart
- 🔮 Predict tomorrow's temperature using Moving Average
- 📥 Export the final report as a CSV file
- 🖥️ Interactive Streamlit dashboard

##🛠️ Technologies Used

- Python
- Pandas – Data processing and analysis
- Matplotlib – Data visualization
- Streamlit – Interactive dashboard

##📁 Project Structure

Weather-Data-Analytics/
│
├── weather_data.csv
├── weather_analytics.py
├── app.py
├── temperature_trend.png
├── weather_distribution.png
├── average_temperature_city.png
├── weather_final_report.csv
└── README.md

##📊 CSV Dataset Format

The input CSV file should contain the following columns:

Column| Description
Date| Date of weather observation
City| Name of the city
Temperature| Temperature in Celsius
Weather| Weather condition such as Sunny, Rainy, Cloudy

##Example:

Date,City,Temperature,Weather
2026-08-01,Delhi,35,Sunny
2026-08-02,Delhi,33,Rainy
2026-08-03,Delhi,36,Sunny

##🚀 Installation

Install the required Python libraries:

pip install pandas matplotlib streamlit

##▶️ How to Run

Run Python Analytics

python weather_analytics.py

This will:

1. Read the CSV dataset.
2. Analyze temperature and weather conditions.
3. Generate charts.
4. Predict tomorrow's temperature.
5. Create "weather_final_report.csv".

Run Streamlit Dashboard

streamlit run app.py

Upload your "weather_data.csv" file in the dashboard to view the analysis interactively.

🔮 Moving Average Prediction

The project uses a 3-day moving average to predict tomorrow's temperature.

The prediction is calculated using:

Predicted Temperature =
Average of the latest 3 daily temperatures

This provides a simple way to estimate the next day's temperature based on recent observations.

📈 Visualizations

The project generates:

1. Temperature Trend

Shows how the average temperature changes over time.

2. Weather Distribution

Displays the number of days for each weather condition.

3. Average Temperature per City

Compares the average temperature of different cities.

##📤 Output

The project generates a final CSV report:

weather_final_report.csv

The report contains:

- City
- Average Temperature
- Hottest City
- Hottest Temperature
- Coldest City
- Coldest Temperature
- Rainy Days
- Sunny Days
- Predicted Tomorrow Temperature

##🎯 Learning Outcomes

Through this project, we learn:

- CSV data handling
- Data cleaning and processing
- Pandas "groupby()" operations
- Statistical calculations
- Data visualization with Matplotlib
- Moving Average
- CSV report generation
- Streamlit dashboard development

#⭐ Conclusion

The Weather Data Analytics System demonstrates how Python can be used to transform raw weather data into meaningful insights through data analysis, visualization, prediction, and interactive dashboards.
# day 25
##📌 Description
The Fraud Detection & Transaction Analysis System is a Python-based data analysis project designed to analyze financial transactions and identify potentially suspicious activities.
The system reads transaction data from a CSV file, detects duplicate and high-value transactions, identifies frequently active accounts, calculates a risk score, generates visualizations, and exports suspicious transactions into a separate CSV file.
##✨ Features
📂 Read transaction data from CSV
🔍 Detect duplicate transactions
💰 Identify high-value transactions
👤 Find accounts with frequent transactions
⚠️ Calculate a risk score for transactions
🚨 Classify transactions into Low, Medium, and High Risk
📊 Generate transaction category chart
📈 Generate daily transaction trend
💵 Display Top 10 highest-value transactions
📁 Export suspicious transactions to CSV
📋 Display transaction analysis summary
@@🛠️ Technologies Used
Python
Pandas – Data processing and analysis
Matplotlib – Data visualization
CSV – Transaction data
#day26
##📄 AI Resume Screening Tool
##📌 Description
The AI Resume Screening Tool is a Python-based application that automatically analyzes multiple resumes and compares them with a given Job Description (JD).
It extracts important candidate information such as Name, Skills, Experience, and Education, calculates a Resume Match Score, ranks candidates according to their scores, identifies missing skills, and exports shortlisted candidates into a CSV file.
The project also includes a Streamlit interface for easy resume uploading and screening.
##✨ Features
📂 Read multiple TXT resume files
👤 Extract candidate names
🛠️ Extract technical skills
💼 Extract work experience
🎓 Extract education details
📋 Analyze Job Description
🔍 Match candidate skills with required skills
📊 Calculate Resume Match Score
🏆 Rank candidates
❌ Highlight missing skills
✅ Shortlist candidates based on score
📥 Export shortlisted candidates to CSV
🌐 Streamlit web interface
##🛠️ Technologies Used
Python
Pandas
Regular Expressions (Regex)
Streamlit
CSV
TXT Files
# DAY 27 
## Description
Python project that analyzes social media data to find trending hashtags, active users, engagement, popular posting times, and content categories.
## Features
Top 5 Trending Hashtags
Most Active Users
Engagement Analysis
Popular Posting Time
Daily Engagement Trend
Content Category Distribution
Sentiment Analysis
CSV Analytics Report
Streamlit Dashboard with Search & Filters
## Technologies
Python
Pandas
Matplotlib
TextBlob
Streamlit
## Run
day27.py
# Day 28
A Python project that analyzes stock portfolio data and calculates investment performance, profit/loss, portfolio returns, and sector-wise investments.
## Features
* Calculate investment for each stock
* Calculate Profit/Loss
* Identify best and worst performing stocks
* Calculate overall portfolio return
* Generate portfolio growth chart
* Generate sector-wise investment chart
* Analyze daily returns
* Predict next-day trend using Moving Average
* Interactive Streamlit dashboard
##  Technologies Used
* Python
