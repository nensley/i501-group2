import streamlit as st
import pandas as pd
import pickle
from prep_data import load_and_preprocess_data, save_processed_data
from model import train_and_save_model
from preprocess_input import preprocess_input_data
import os

def main():
    st.title("Income Prediction Model")
    
    # Paths for data and model files
    input_file_path = 'data/adult.data.csv'  # Adjust this to the correct path to your data file
    output_file_path = 'data/processed_data.csv'  # Path where the processed data will be saved
    model_path = 'data/trained_model.pkl'  # Path where the model is stored
    
    # Step 1: Load and preprocess the data
    if not os.path.exists(output_file_path):
        processed_df = load_and_preprocess_data(input_file_path)
        save_processed_data(processed_df, output_file_path)
          
    # Step 2: Train and Save the Model (if not already saved)
    if not os.path.exists(model_path):
        train_and_save_model(output_file_path, model_path)
        
    # Step 3: Load the trained model
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    
    # Step 4: User Inputs (Dropboxes for sex, education, occupation, and race)
    st.subheader("Please select:")

    age = st.number_input("Age", min_value=17, max_value=100)

    sex = st.selectbox("Sex", ("Male", "Female"))

    education = st.selectbox(
        "Education", ("Doctorate", "Professional School", "Masters", "Bachelors", "Associates", "Some College", "HS Grad")
    )

    occupation = st.selectbox(
        "Occupation",
        (
            "Executive/Management", "Professional Specialty", "Construction/Repair", "Administrative/Clerical", 
            "Sales", "Logistics/Transportation", "Machine Operator", "Janitor", "Agricultural/Fishing", 
            "Public Safety", "Housekeeper", "Armed Forces", "Tech Support", "Other Service Roles"
        ),
    )

    hours_worked = st.number_input("Hours Worked Per Week", placeholder="Input your Weekly Hours")

    race = st.selectbox("Race", ("White", "Black", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other"))
    
    # Step 5: Preprocess User Input
    input_data = preprocess_input_data(age, sex, education, occupation, race, hours_worked)
    
    # Step 6: Prediction
    if st.button("Predict Income"):
        prediction = model.predict(input_data)
        income_category = ">50K" if prediction[0] == 1 else "<=50K"
        st.write(f"Predicted Income Category: {income_category}")

if __name__ == '__main__':
    main()
