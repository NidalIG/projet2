import pandas as pd

# Création du DataFrame à partir des données
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

# Calculer le nombre de personnes par race
def race_count(df):
    return df['race'].value_counts()

# Calculer l'âge moyen des hommes
def average_age_men(df):
    average_men = df[df['sex'] == 'Male']
    return average_men['age'].mean()

# Calculer le pourcentage de personnes ayant un Bachelor
def percentage_bachelor(df):
    person_bachelor = df[df['education'] == 'Bachelors']
    return (len(person_bachelor) / len(df)) * 100

# Calculer le pourcentage de personnes ayant un diplôme avancé et un salaire >50K
def percentage_advanced_education_high_salary(df):
    advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    advanced_education_high_salary = advanced_education[advanced_education['salary'] == '>50K']
    return (len(advanced_education_high_salary) / len(advanced_education)) * 100

# Calculer le pourcentage de personnes sans diplôme avancé avec un salaire >50K
def percentage_no_advanced_education_high_salary(df):
    no_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    no_advanced_education_high_salary = no_advanced_education[no_advanced_education['salary'] == '>50K']
    return (len(no_advanced_education_high_salary) / len(no_advanced_education)) * 100

# Trouver le nombre minimum d'heures travaillées par semaine
def min_hour_work(df):
    return df['hours-per-week'].min()

# Calculer le pourcentage des personnes qui travaillent le minimum d'heures et gagnent plus de 50K
def percentage_work_min_salarymorethan50(df, min_hour_work):
    person_work_min = df[df['hours-per-week'] == min_hour_work]
    work_min_salarymorethan50 = len(person_work_min[person_work_min['salary'] == '>50K'])
    return (work_min_salarymorethan50 / len(person_work_min)) * 100

# Trouver le pays avec le pourcentage le plus élevé de personnes gagnant plus de 50K
def country_highest_percentage_earning_50K(df):
    country_earning_50K = df.groupby('native-country').apply(lambda x: (x[x['salary'] == '>50K'].shape[0] / x.shape[0]) * 100)
    highest_percentage_country = country_earning_50K.idxmax()
    highest_percentage_value = country_earning_50K.max()
    return highest_percentage_country, highest_percentage_value

# Trouver la profession la plus populaire en Inde parmi ceux qui gagnent plus de 50K
def most_popular_occupation_in_india(df):
    india_high_salary = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    if not india_high_salary.empty:
        return india_high_salary['occupation'].mode()[0]  # Retourne la première valeur de la mode
    else:
        return "No data for India with salary >50K"  # Message d'erreur si aucune donnée ne correspond

