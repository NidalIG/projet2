import pandas as pd
from demographic_data_analyzer import (
    race_count,
    average_age_men,
    percentage_bachelor,
    percentage_advanced_education_high_salary,
    percentage_no_advanced_education_high_salary,
    min_hour_work,
    percentage_work_min_salarymorethan50,
    country_highest_percentage_earning_50K,
    most_popular_occupation_in_india
)

# Créez le DataFrame à partir des mêmes données utilisées dans le fichier principal
data = {
    'age': [39, 50, 38, 53, 28],
    'workclass': ['State-gov', 'Self-emp-not-inc', 'Private', 'Private', 'Private'],
    'fnlwgt': [77516, 83311, 215646, 234721, 338409],
    'education': ['Bachelors', 'Bachelors', 'HS-grad', '11th', 'Bachelors'],
    'education-num': [13, 13, 9, 7, 13],
    'marital-status': ['Never-married', 'Married-civ-spouse', 'Divorced', 'Married-civ-spouse', 'Married-civ-spouse'],
    'occupation': ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 'Handlers-cleaners', 'Prof-specialty'],
    'relationship': ['Not-in-family', 'Husband', 'Not-in-family', 'Husband', 'Wife'],
    'race': ['White', 'White', 'White', 'Black', 'Black'],
    'sex': ['Male', 'Male', 'Male', 'Male', 'Female'],
    'capital-gain': [2174, 0, 0, 0, 0],
    'capital-loss': [0, 0, 0, 0, 0],
    'hours-per-week': [40, 13, 40, 40, 40],
    'native-country': ['United-States', 'United-States', 'United-States', 'United-States', 'Cuba'],
    'salary': ['<=50K', '<=50K', '<=50K', '<=50K', '<=50K']
}
df = pd.DataFrame(data)

# Tester les fonctions
print("Race count:")
print(race_count(df))

print("Average age of men:")
print(average_age_men(df))

print("Percentage of people with a Bachelor's degree:")
print(percentage_bachelor(df))

print("Percentage of people with advanced education and salary > 50K:")
print(percentage_advanced_education_high_salary(df))

print("Percentage of people without advanced education and salary > 50K:")
print(percentage_no_advanced_education_high_salary(df))

min_hours = min_hour_work(df)
print(f"Minimum hours worked per week: {min_hours}")
print("Percentage of people who work the minimum number of hours and earn >50K:")
print(percentage_work_min_salarymorethan50(df, min_hours))

highest_country, highest_percentage = country_highest_percentage_earning_50K(df)
print(f"Country with highest percentage earning >50K: {highest_country} ({highest_percentage:.1f}%)")

print("Most popular occupation for people earning >50K in India:")
print(most_popular_occupation_in_india(df))
