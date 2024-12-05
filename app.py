import streamlit as st
import pandas as pd
import pickle
from prep_data import load_and_preprocess_data, save_processed_data
from model import IncomeModelTrainer
from preprocess_input import preprocess_input_data
from visualization import create_income_distribution_plot
import os

def main():
    # Add Title and heading
    st.write("""
    # Income Prediction Model

    This app predicts whether the income is >50K or <=50K

    Dataset: Becker, B. & Kohavi, R. (1996). Adult [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5XW20.""")
    
    # Paths for data and model files
    input_file_path = 'data/adult.data.csv'  # Adjust this to the correct path to your data file
    output_file_path = 'data/processed_data.csv'  # Path where the processed data will be saved
    model_path = 'trained_model.pkl'  # Path where the model is stored

    # initialize the income model class
    income_model = IncomeModelTrainer(model_save_path=model_path)
    
    # Step 1: Load and preprocess the data
    if not os.path.exists(output_file_path):
        processed_df = load_and_preprocess_data(input_file_path)
        save_processed_data(processed_df, output_file_path)
          
    # Step 2: Train and Save the Model (if not already saved)
    if not os.path.exists(model_path):
        income_model.train_model()
        income_model.save_model()
    
    # Cache the model in memory
    @st.cache_data
    # define the function to load and cache the model
    def load_and_cache_model():
        try:
            # Load the model and preprocessor from python class
            model, preprocessor = income_model.load_model()  # Ensure parentheses to call the method
            return model, preprocessor
        except Exception as e:
            # Handle error if the model is not loaded
            st.error(f"Error loading model: {e}")
            st.stop()  # Stop the application if the model cannot be loaded

    # Call the function to load and cache the model
    model, preprocessor = load_and_cache_model()
    
    # Step 4: User Inputs (Dropboxes for sex, education, occupation, and race)
    st.sidebar.subheader("Please select:")

    age = st.sidebar.slider("Age", 17, 100, 25)

    sex = st.sidebar.selectbox("Sex", ("Male", "Female"))

    education = st.sidebar.selectbox(
        "Education", ("Doctorate", "Professional School", "Masters", "Bachelors", "Associates", "Some College", "HS Grad")
    )

    occupation = st.sidebar.selectbox(
        "Occupation",
        (
            "Executive/Management", "Professional Specialty", "Construction/Repair", "Administrative/Clerical", 
            "Sales", "Logistics/Transportation", "Machine Operator", "Janitor", "Agricultural/Fishing", 
            "Public Safety", "Housekeeper", "Armed Forces", "Tech Support", "Other Service Roles"
        ),
    )

    hours_worked = st.sidebar.slider("Hours Worked Per Week", 0, 99, 40)

    race = st.sidebar.selectbox("Race", ("White", "Black", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other"))
    
    # Step 5: Preprocess User Input
    input_data = preprocess_input_data(age, sex, education, occupation, race, hours_worked)
    processed_input_data = preprocessor.transform(input_data)

    # Step 6: Prediction
    if st.button("Predict Income"):
        # uses the model to make prediction based on input data
        prediction = model.predict(processed_input_data)
        prediction_value = prediction[0]
        # Set the color based on the prediction value
        if prediction_value == '<=50K':
            box_color = 'salmon'
        else:
            box_color = 'skyblue'

        # Display the prediction with the corresponding box color, bold black text
        st.markdown(f"<div style='background-color:{box_color}; padding: 10px; font-size: 16px; font-weight: bold; color: black;'>Predicted Income Category: {prediction_value}</div>", unsafe_allow_html=True)

    # Step 7: Visualization
        user_inputs = {
            'age': age,
            'sex': sex,
            'education': education,
            'occupation': occupation,
            'race': race,
            'hours_worked': hours_worked
        }

        fig = create_income_distribution_plot(output_file_path, user_inputs, prediction_value)
        # st.pyplot(fig)
        st.plotly_chart(fig)

if __name__ == '__main__':
    main()
