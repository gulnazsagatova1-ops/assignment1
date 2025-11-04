This is a final project assignment for Coding for Economists classes
by Gulnaz Sagatova

The dataset **`food-health.csv`** includes information about people’s eating habits and several health indicators such as BMI, cholesterol, and blood pressure. The main idea of this project is to look at how eating habits might be related to basic health conditions.  

My main goal was to practice data cleaning and analysis using **Python** and **Stata** for data cleaning, organization, and simple analysis. 


## Folder structure
- In data folder you can download data
- In code folder you can see both python and stata codes 

## How to reproduce the work 
### Python
1. Open VS Code 
2. Navigate to project folder "Code"
3. Run the Python script
   python code/final_project.py

### Stata
1. Open Stata
Set your working directory to: cd "/Users/Sagatova_Gulnaz/Desktop/coding/"
2. Navigate to project folder "Code"
3. Run the do file: do code/final_project.do

## Result of the work
After running either code you can get:
1) Cleaned dataset
2) Two Graphs

## What the Python code does
1) Import libraries
Uses pandas, numpy, matplotlib, and seaborn.
2) Read data
Loads food-health.csv from the data/ folder.
3) Clean data
Replaces missing values (?, NA, etc.) with NaN.
Fills numeric columns with the column mean.
Fills categorical columns with the most frequent (mode) value.
4) Use lists and dictionaries
A list stores numeric column names.
A dictionary stores average health metrics (BMI, weight, cholesterol).
5) Filter and transform data
Keeps only rows with BMI between 18.5 and 30
Selects specific columns
6) Creates two new variables:
w_h_ratio which is weight-to-height ratio
log_cholesterol which is log-transformed cholesterol
7) Save cleaned data
Saves the filtered dataset as
data/food-health-cleaned.csv.
8) Create summary statistics
Prints key descriptive statistics using data.describe().
9) Visualize data
Histogram of BMI
Scatter plot of BMI vs Total Cholesterol

## What the Stata code does
1) Import data
Reads data/food-health.csv
2) Clean data
Replaces invalid symbols (NA, ?, spaces) with missing
Converts numeric text fields
Fills missing numeric data with means.
3) Filter and transform data
Keeps normal BMI between 18.5 and 30.
Selects relevant columns
Creates new variables (w_h_ratio, log_cholesterol).
4) Saves cleaned data 
5) Create summary statistics
6) Visualize data:
Histogram showing BMI distribution
Scatter plot showing BMI vs Total Cholesterol
Both graphs exported as .png files
