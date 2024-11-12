import os
from dotenv import load_dotenv
import streamlit as st

# Dropdowns (Occupation, Race, Sex, and Education)
st.title("Income Analysis")
st.subheader("Please select:", divider="gray")

age = st.number_input(
    "Age", value=None, placeholder="Input your Age"
)

Sex = st.selectbox(
	"Sex", ("Male", "Female"),
	placeholder  = "Choose your Sex",)

Education = st.selectbox(
	"Education", ("Doctorate", "Professional School", "Masters", "Bachelors", "Associates", "Some-college", "HS grad"),
	placeholder = "Choose your Education",)

Occupation = st.selectbox(
	"Occupation",
	("Executive/Management", "Professional Speciality", "Construction/Repair", "Administrative/Clerical", "Sales", "Logistics/Transportation", "Machine Operator", "Janitor", "Agricultural/Fishing", "Public Safety", "Housekeeper", "Armed Forces", "Tech Support", "Other Service Roles"),
	placeholder="Choose your Occupation",
)

Hours_worked = st.number_input(
    "Hours Worked Per Week", value=None, placeholder="Input your Weekly Hours"
)

Race = st.selectbox(
	"Race", ("White", "Black'", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other"),
    placeholder = "Choose your Race", )