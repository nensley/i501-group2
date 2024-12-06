import pandas as pd

def preprocess_input_data(age, sex, education, occupation, race, hours_worked):

     # Create a DataFrame with the user input
    input_data = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'education': [education],
        'occupation': [occupation],
        'race': [race],
        'hours_worked': [hours_worked]
    })

    education_mapping = {
        "Doctorate": 24, 
        "Professional School": 22,
        "Masters": 18, 
        "Bachelors": 16, 
        "Associates": 14, 
        "Some College": 13, 
        "HS Grad": 12
    }

    # Create new column for education-yr
    input_data['education-yr'] = input_data['education'].map(education_mapping)

    # create mapping for occupation
    occupation_mapping = {
        "Executive/Management": "Exec-managerial", 
        "Professional Specialty": "Prof-specialty", 
        "Construction/Repair": "Craft-repair", 
        "Administrative/Clerical": "Adm-clerical", 
        "Sales": "Sales", 
        "Logistics/Transportation": "Transport-moving", 
        "Machine Operator": "Machine-op-inspct", 
        "Janitor": "Handlers-cleaners", 
        "Agricultural/Fishing": "Farming-fishing", 
        "Public Safety": "Protective-serv", 
        "Housekeeper": "Priv-house-serv", 
        "Armed Forces": "Armed-Forces", 
        "Tech Support": "Tech-support", 
        "Other Service Roles": "Other-service",
    }

    # Use mapping to update occupation column
    input_data['occupation'] = input_data['occupation'].map(occupation_mapping)

    # Categorize Age Group
    input_data['age-group'] = input_data['age'].apply(lambda x: '35+' if x >= 35 else '17-34')

     # Standardize Race categories
    race_mapping = {
        "Asian or Pacific Islander": "Asian-Pac-Islander",
        "American Indian or Eskimo": "Amer-Indian-Eskimo"
    }
    input_data['race'] = input_data['race'].map(race_mapping).fillna(input_data['race'])

    # Categorize Hours Worked as Employment Type
    def categorize_employment_type(hours):
        if hours < 35:
            return 'part_time'
        elif 35 <= hours <= 40:
            return 'full_time'
        else:
            return 'over_time'

    input_data['employment-type'] = input_data['hours_worked'].apply(categorize_employment_type)

    # Drop the original age and hours_worked columns, as they’ve been converted
    input_data = input_data.drop(columns=['age', 'hours_worked'])

    # Reorder the columns to match the expected order
    input_data = input_data[['age-group', 'sex', 'education-yr', 'occupation', 'employment-type', 'race']]

    return input_data