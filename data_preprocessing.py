import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

def preprocess_data(df):
    # Handling missing values
    numeric_features = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = df.select_dtypes(include=['object']).columns

    numeric_transformer = SimpleImputer(strategy='mean')
    categorical_transformer = SimpleImputer(strategy='constant', fill_value='missing')

    # Normalizing numerical columns
    numeric_transformer = StandardScaler()

    # Encoding categorical columns
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    df_processed = preprocessor.fit_transform(df)
    return df_processed

# Example usage:
data = {
    'age': [25, 30, 35, None, 40],
    'salary': [50000, 60000, None, 80000, 90000],
    'gender': ['M', 'F', None, 'F', 'M']
}
df = pd.DataFrame(data)
processed_data = preprocess_data(df)
print(processed_data)
