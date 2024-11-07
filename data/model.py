# import pandas
import pandas as pd
# import modeling characteristics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Equal Sample of Both Greater than 50K and Less than 50K
df_greater_50k = df_census[df_census['income'] == '>50K']
df_less_equal_50k = df_census[df_census['income'] == '<=50K']
n_samples = 5000
greater_sample = df_greater_50k.sample(n=n_samples, random_state=42)
less_sample = df_less_equal_50k.sample(n=n_samples, random_state=42)
df_census_subset = pd.concat([greater_sample, less_sample])

# Model features
X = df_census_subset[['education-yr', 'occupation', 'type-of-employment', 'sex', 'age_group', 'race']]
# Target Model Feature
y = df_census_subset['income']

# Convert Categorical Variables into Boolean Values for model
y = pd.get_dummies(y, drop_first=True)
X = pd.get_dummies(X, drop_first=True)

# Split data into Training and Testing Data Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=60)

# Train Logistic Regression Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)