# import pandas
import pandas as pd
# import modeling characteristics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import pickle

# python class to store different functions of model training and saving
class IncomeModelTrainer:
    # initialize the model trainer with proper paths
    def __init__(self, processed_data_path = 'data/processed_data.csv', model_save_path='trained_model.pkl'):
        # initialize model attributes to store data paths, model, and preprocessor
        self.processed_data_path = processed_data_path
        self.model_save_path = model_save_path
        self.model = None
        self.preprocessor = None

    # train model function
    def train_model(self, n_samples = 5000):
        df = pd.read_csv(self.processed_data_path)
        # Equal Sample of Both Greater than 50K and Less than 50K
        df_greater_50k = df[df['income'] == '>50K']
        df_less_equal_50k = df[df['income'] == '<=50K']
        greater_sample = df_greater_50k.sample(n=n_samples, random_state=42)
        less_sample = df_less_equal_50k.sample(n=n_samples, random_state=42)
        df_subset = pd.concat([greater_sample, less_sample])

        # Model features
        X = df_subset[['education-yr', 'occupation', 'employment-type', 'sex', 'age-group', 'race']]
        # Target Model Feature
        y = df_subset['income']

        # Define preprocessor to encode categorical features
        preprocessor = ColumnTransformer(
            transformers=[
                ('cat', OneHotEncoder(), ['education-yr', 'occupation', 'employment-type', 'sex', 'age-group', 'race'])
            ], remainder='passthrough'
        )

        # Transform input variables using preprocessor
        X_transformed = preprocessor.fit_transform(X)

        # Split data into Training and Testing Data Sets
        X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.3, random_state=60)

        # Train Logistic Regression Model
        self.model = LogisticRegression(max_iter=1000)
        self.model.fit(X_train, y_train)

    # function to train the model and save it to model_path
    def save_model(self):
        # if the model or preprocessor are not present, raise an error
        if self.model == None or self.preprocessor == None:
            raise ValueError("Model and preprocessor must be trained before saving.")

        # Save the model and preprocesser using pickle
        with open('trained_model.pkl', 'wb') as f:
            pickle.dump({'model': model, 'preprocessor': preprocessor}, f)
    
    def load_model(self):
        # open and unpickle the model and preprocessor
        with open(self.model_save_path, 'rb') as f:
            saved_data = pickle.load(f)
            model = saved_data['model']
            preprocessor = saved_data['preprocessor']   
        # return model and preprocessor
        return model, preprocessor