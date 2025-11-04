# Food-Health 

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Task 1
data = pd.read_csv("/Users/gulnazsagatova/Desktop/dt1/task1/data/food-health.csv")

# Data Exploration
data.head(10)
data.describe()
data.info()
data.dtypes

# Task 5
# Replace missing values with NaN
data = data.replace(["?", "NA", "NaN", " "], pd.NA)

# Separate numeric and categorical columns
num_cols = data.select_dtypes(include=['number']).columns
cat_cols = data.select_dtypes(include=['object', 'category']).columns

# Fill numeric missing with mean, categorical with mode
for col in num_cols:
    data[col] = data[col].fillna(data[col].mean())

for col in cat_cols:
    data[col] = data[col].fillna(data[col].mode()[0])

# Task 2 and 3
# List of important numeric columns
numeric_cols = ['bp_diastolic', 'total_cholesterol', 'hdl', 'weight', 'height', 'ldl', 'bmi']

# Loop through list to print averages (automation)
for col in numeric_cols:
    print(f"{col}: mean = {data[col].mean():.2f}")

# Dictionary example for summary values
health_means = {
    'Average BMI': data['bmi'].mean(),
    'Average Weight': data['weight'].mean(),
    'Average Cholesterol': data['total_cholesterol'].mean()
}
print(health_means)

# Task 6
# a) Filter observations 
filtered_data = data[(data['bmi'] >= 18.5) & (data['bmi'] <= 30)]

# b) Filter variables 
filtered_data = filtered_data[['weight', 'height', 'bmi', 'total_cholesterol', 'hdl', 'ldl', 'heart_risk']]

# c) Create new variables 
filtered_data['w_h_ratio'] = filtered_data['weight'] / filtered_data['height']
filtered_data['log_cholesterol'] = np.log(filtered_data['total_cholesterol'])

# Task 7
filtered_data.to_csv("/Users/gulnazsagatova/Desktop/dt1/task1/data/food-health-cleaned.csv", index=False)

# Task 8
summary = data.describe()
print(summary)

#Task 9
# Histogram of BMI
plt.hist(data['bmi'], bins=30)
plt.title("Distribution of BMI")
plt.xlabel("BMI")
plt.ylabel("Frequency")
plt.show()

# Scatter plot: BMI vs Total Cholesterol
sns.scatterplot(x='bmi', y='total_cholesterol', data=data)
plt.title("BMI vs Total Cholesterol")
plt.show()

# The End.
# Thank you for your attention!