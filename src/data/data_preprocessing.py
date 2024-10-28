# data/data_preprocessing.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer
from typing import Tuple, List, Dict

class DataPreprocessor:
    def __init__(self, df: pd.DataFrame):
        """
        Initialize the DataPreprocessor with a DataFrame.
        :param df: DataFrame to preprocess.
        """
        self.df = df

    def clean_data(self) -> pd.DataFrame:
        """
        Clean the DataFrame by handling missing values and duplicates.
        :return: Cleaned DataFrame.
        """
        # Remove duplicates
        self.df.drop_duplicates(inplace=True)

        # Handle missing values
        imputer = SimpleImputer(strategy='mean')
        for column in self.df.select_dtypes(include=[np.number]).columns:
            self.df[column] = imputer.fit_transform(self.df[[column]])

        # For categorical columns, fill missing values with the mode
        for column in self.df.select_dtypes(include=[object]).columns:
            self.df[column].fillna(self.df[column].mode()[0], inplace=True)

        return self.df

    def encode_labels(self, column: str) -> pd.DataFrame:
        """
        Encode categorical labels into numerical values.
        :param column: Column name to encode.
        :return: DataFrame with encoded labels.
        """
        le = LabelEncoder()
        self.df[column] = le.fit_transform(self.df[column])
        return self.df

    def one_hot_encode(self, columns: List[str]) -> pd.DataFrame:
        """
        One-hot encode specified categorical columns.
        :param columns: List of column names to one-hot encode.
        :return: DataFrame with one-hot encoded columns.
        """
        self.df = pd.get_dummies(self.df, columns=columns, drop_first=True)
        return self.df

    def split_data(self, target_column: str, test_size: float = 0.2, random_state: int = 42) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        """
        Split the DataFrame into training and testing sets.
        :param target_column: Name of the target column.
        :param test_size: Proportion of the dataset to include in the test split.
        :param random_state: Random seed for reproducibility.
        :return: X_train, X_test, y_train, y_test.
        """
        X = self.df.drop(columns=[target_column])
        y = self.df[target_column]
        return train_test_split(X, y, test_size=test_size, random_state=random_state)

    def scale_features(self, feature_columns: List[str]) -> pd.DataFrame:
        """
        Scale features using StandardScaler.
        :param feature_columns: List of feature column names to scale.
        :return: DataFrame with scaled features.
        """
        scaler = StandardScaler()
        self.df[feature_columns] = scaler.fit_transform(self.df[feature_columns])
        return self.df

    def feature_engineering(self, new_column_name: str, operation: str, columns: List[str]) -> pd.DataFrame:
        """
        Create a new feature based on existing columns.
        :param new_column_name: Name of the new column.
        :param operation: Operation to perform ('sum', 'mean', 'product').
        :param columns: List of columns to use for the operation.
        :return: DataFrame with the new feature.
        """
        if operation == 'sum':
            self.df[new_column_name] = self.df[columns].sum(axis=1)
        elif operation == 'mean':
            self.df[new_column_name] = self.df[columns].mean(axis=1)
        elif operation == 'product':
            self.df[new_column_name] = self.df[columns].prod(axis=1)
        else:
            raise ValueError("Unsupported operation. Use 'sum', 'mean', or 'product'.")
        return self.df

    def remove_outliers(self, column: str, threshold: float = 1.5) -> pd.DataFrame:
        """
        Remove outliers from a specified column using the IQR method.
        :param column: Column name to check for outliers.
        :param threshold: IQR multiplier to define outliers.
        :return: DataFrame with outliers removed.
        """
        Q1 = self.df[column].quantile(0.25)
        Q3 = self.df[column].quantile(0.75)
        IQR = Q3 - Q1
 self.df = self.df[~((self.df[column] < (Q1 - threshold * IQR)) | (self.df[column] > (Q3 + threshold * IQR)))]
        return self.df

# Example usage
if __name__ == "__main__":
    # Load data
    data_loader = DataLoader(data_dir='path/to/data')
    df = data_loader.load_data('data.csv', file_type='csv')

    # Preprocess data
    preprocessor = DataPreprocessor(df)
    df = preprocessor.clean_data()
    df = preprocessor.encode_labels('target_column')
    df = preprocessor.one_hot_encode(['category_column1', 'category_column2'])
    X_train, X_test, y_train, y_test = preprocessor.split_data('target_column')
    X_train = preprocessor.scale_features(['feature_column1', 'feature_column2'])
    X_train = preprocessor.feature_engineering('new_column', 'sum', ['column1', 'column2'])
    X_train = preprocessor.remove_outliers('column_with_outliers')
