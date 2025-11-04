This is a final project assignment for Coding for Economists classes

## Folder Structure
In data folder you can download data 
In code folder you can see both python and stata codes 

## How to Reproduce the Work
1. Open VS Code 
2. Navigate to project folder "Code"
3. Run the Python script
   python code/final_project.py
4. The script will:
Read data/food-health.csv
Fix missing values and data types
Filter and transform data
Create summary statistics
Generate graphs (BMI distribution, BMI vs Cholesterol)
5. Output
After running the script, you’ll get:
Cleaned dataset: data/food-health-cleaned.csv
Two graphs


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
Keeps only rows with BMI between 18.5 and 30.
Selects specific columns.
6) Creates two new variables:
w_h_ratio → weight-to-height ratio
log_cholesterol → log-transformed cholesterol

7) Save cleaned data
Saves the filtered dataset as
data/food-health-cleaned.csv.
8) Create summary statistics
Prints key descriptive statistics using data.describe().
9) Visualize data
Histogram of BMI
Scatter plot of BMI vs Total Cholesterol
