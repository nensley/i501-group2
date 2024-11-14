# import pandas
import pandas as pd
# import modeling characteristics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# function to train the model and save it to model_path
def train_and_save_model(processed_data_path, model_path):
    # load the dataset
    df = pd.read_csv('data\adult.data.csv')

    # Equal Sample of Both Greater than 50K and Less than 50K
    df_greater_50k = df[df['income'] == '>50K']
    df_less_equal_50k = df[df['income'] == '<=50K']
    n_samples = 5000
    greater_sample = df_greater_50k.sample(n=n_samples, random_state=42)
    less_sample = df_less_equal_50k.sample(n=n_samples, random_state=42)
    df_subset = pd.concat([greater_sample, less_sample])

    # Model features
    X = df_subset[['education-yr', 'occupation', 'employment-type', 'sex', 'age-group', 'race']]
    # Target Model Feature
    y = df_subset['income']

    # Convert Categorical Variables into Boolean Values for model
    y = pd.get_dummies(y, drop_first=True)
    X = pd.get_dummies(X, drop_first=True)

    # Split data into Training and Testing Data Sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=60)

    # Train Logistic Regression Model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Save the model using pickle
    with open('trained_model.pkl', 'wb') as f:
        pickle.dump(model, f)