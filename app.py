import os
from dotenv import load_dotenv
import streamlit as st

st.write(
'''
## Income Predictor

Predict whether your income is greater than or less than 50K.
'''
)

# Text Input
text = st.text_input("Please put your information below.")

# Number and Drop Down inputs for Age, Sex, Education, Occupation, Race, and Hours Worked
age = st.number_input(
    "Age", value=None, placeholder="Input your Age"
)

Sex = st.selectbox(
	"Sex", ("Male", "Female", "Prefer to not say"),
Index = None,
placeholder  = "Choose your Sex",)

Education = st.selectbox(
	"Education", ("Doctorate", "Professional School", "Masters", "Bachelors", "Associates", "Some-college", "HS grad"),
Index = None,
Placeholder = "Choose your Education",)

Occupation = st.selectbox(
	"Occupation",
	("Executive/Management", "Professional Specialty", "Construction/Repair", "Administrative/Clerical", "Sales", "Logistics/Transportation", "Machine Operator", "Janitor", "Agricultural/Fishing", "Public Safety", "Housekeeper", "Armed Forces", "Tech Support", "Other Service Roles"),
Index = None,
placeholder="Choose your Occupation",
)

hours-worked = st.number_input(
    "Hours Worked Per Week", value=None, placeholder="Input your Weekly Hours"
)

Race = st.selectbox(
	"Race", ("White", "Black'", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other"),
Index = None,
placeholder = "Choose your Race", )
