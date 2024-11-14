# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# make a function that loads the data and preprocesses it
def load_and_preprocess_data(file_path):

    # open dataframe to work with
    df = pd.read_csv(file_path)

    # remove the leading space of every value in columns containing string data
    df['sex'] = df['sex'].str.strip()
    df['workclass'] = df['workclass'].str.strip()
    df['education'] = df['education'].str.strip()
    df['marital-status'] = df['marital-status'].str.strip()
    df['occupation'] = df['occupation'].str.strip()
    df['relationship'] = df['relationship'].str.strip()
    df['race'] = df['race'].str.strip()
    df['native-country'] = df['native-country'].str.strip()
    df['income'] = df['income'].str.strip()

    # replace the question marks (marking missing data) with a standardized missing data format
    df.replace('?', np.nan)

    # Remove rows with missing values
    df = df.dropna()

    # Add New Columns for Model

    # Column 1: education-yr
    # make a mapping for education-yr based on education value
    # mapping is based on years of school completed
    mapping = {'10th': 10, 
            '11th': 11, 
            '12th': 12, 
            '1st-4th': 4,
            '5th-6th': 6,
            '7th-8th': 8,
            '9th': 9,
            'Assoc-acdm': 14,
            'Assoc-voc': 14,
            'Bachelors': 16,
            'Doctorate': 24,
            'HS-grad': 12,
            'Masters': 18,
            'Preschool': 0,
            'Prof-school': 22,
            'Some-college': 13
            }

    # Create new column for education-yr
    df['education-yr'] = df['education'].map(mapping)

    # Column 2: employment-type

    # definitions
    # less than 35 hours = part_time
    # 35-40 hours = full_time
    # More than 40 hours = over_time

    # create a function that classifies employment type by hours per week worked
    def classify_employment(hours):
        if hours < 35:
            return 'part_time'
        elif 35 <= hours <= 40:
            return 'full_time'
        else:
            return 'over_time'

    # Create new column for type of employment using classification function
    df['employment-type'] = df['hours-per-week'].apply(classify_employment)

    # Column 3: age-group

    # make bins for age groups
    custom_bins = [17, 34, 100]
    bin_labels = ['17-34', '35+']

    # Add a new column for age groups based on custom bins
    df['age-group'] = pd.cut(df['age'], bins=custom_bins, labels=bin_labels)

    # returns the processed dataframe
    return df

# save processed data to a given file path
def save_processed_data(df, file_path):
    df.to_csv(file_path)