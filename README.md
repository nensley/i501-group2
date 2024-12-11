# i501-group2

**Link to the Application:** https://incomepredictionmodel.streamlit.app

**Abstract or Overview:** The purpose of the project is to predict the income of an individual through an interactive user interface that allows users to adjust different potential income factors. A stakeholder may look for how certain demographic factors, like race and sex, impact the income of an individual that has similar job qualification. This may indicate pay inequality.

**Data Description:** The data used in the dataset is from a census dataset located at https://doi.org/10.24432/C5XW20. The data is a sample of 48,842 individual instances in the 1994 U.S. census data and includes a variety of demographic values in addition to whether the income of the individual is greater than or less than 50 thousand dollars.

**Algorithm Description:** Data is loaded into the application and preprocessed according to data cleaning measures, including removing rows with missing data and developing new categorical variables from numerical variables using pandas dataframe manipulation methods. This processed data is then saved and used to train a logistic regression model with a binary income target variable. This model, developed using the sklearn package, is then cached in the webpage for frequent use, where it is retrieved from memory and used to make a prediction when a user changes different values in a sidebar and clicks the submit button. Input data is reclassified according to methods saved in the preprocessor and yields a prediction. This prediction is output to a text box on the streamlit application. Additionally, input values are used to get the income percentage values of different parameters, which is output in an interactive stacked bar chart using plotly.

## Tools Used
- **pandas**: Used for data manipulation and preprocessing, such as cleaning and transforming raw data into a usable format.
- **scikit-learn**: Used for implementing the logistic regression model and handling training, testing, and predictions.
- **streamlit**: Provides the framework for creating the interactive web application, including the sidebar for inputs and the prediction display.
- **plotly**: Used for creating interactive visualizations to display income percentages for each parameter.
- **numpy**: Supports numerical computations and handling of arrays where necessary.
- **pickle**: Used to serialize and save the trained logistic regression model for efficient reuse without needing to retrain the model each time the application is launched.

## Ethical Concerns:
  1. **Historical Bias:** Dataset is outdated with census data from 1994. The data only includes two genders, and income is not close to comparable data for the current year, leading users to gain insights that would not apply to their current historical context.

Solution: Get a new dataset with more recent census data from the past few years that also includes more gender designations. Since application is already developed, clear inclusion of when this data was collected is included in the user interface.

  3. **Representation Bias:** The dataset also has a representation bias. Over 85% of the entries are white people, and two thirds of the entries are men. Even at the time of the data, the U.S. was closer to 75% white and 48% men. Thus, the dataset is overrepresenting white people and men. Additionally, the armed forces is underrepresented with less than 1% of entries and creative freelancer roles, like authors and photographers are not even included in the data at all.

  Solution: When training a model, the training sample can be proportioned to include a sample closer to the real proportions of white people and men at the time. However, it is impossible to make up for data that is not present. Thus, to handle the underrepresentation of certain occupations, more data needs to be recorded or a new dataset needs to be used.

  3. **Measurement Bias:** The dataset has a measurement bias in how it records income. Income is recorded as a binary variable, where it is either above 50 thousand or below 50 thousand. This oversimplifies the spectrum of income to a comparison to a single value.

  Solution: The dataset should have been collected with raw income numbers included. Later on, analysis can take place to determine whether 50 thousand is valid point to draw comparison at.

  4. **Evaluation Bias:** In picking the model's parameters, we looked at increasing the accuracy score as high as possible by changing numerical variables into categorical variables, including age and hours per week.

  Solution: Looking at whether the cutoff for age groups is useful needs both a look at how it affects accuracy and how relevant it is at grouping similar data together.

  5. **Inherent Bias:** This model was conceived primarily for interest in how different factors impacted income. However, with the data being outdated and the feature parameter being binary, it's value for insight is minimized. The model serves little value besides being intriguing and practice.

  Solution: Find a new dataset that is more relevant to the current time or at least includes income as a continuous variable.
