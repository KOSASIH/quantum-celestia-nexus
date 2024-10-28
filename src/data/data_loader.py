# data/data_loader.py

import pandas as pd
import os
import json
import numpy as np
from typing import Union, List, Dict

class DataLoader:
    def __init__(self, data_dir: str):
        """
        Initialize the DataLoader with the directory containing the data files.
        :param data_dir: Directory where data files are stored.
        """
        self.data_dir = data_dir

    def load_csv(self, filename: str) -> pd.DataFrame:
        """
        Load a CSV file into a DataFrame.
        :param filename: Name of the CSV file.
        :return: DataFrame containing the data.
        """
        file_path = os.path.join(self.data_dir, filename)
        if os.path.exists(file_path):
            return pd.read_csv(file_path)
        else:
            raise FileNotFoundError(f"{filename} not found in {self.data_dir}")

    def load_json(self, filename: str) -> Union[Dict, List]:
        """
        Load a JSON file into a Python dictionary or list.
        :param filename: Name of the JSON file.
        :return: Dictionary or list containing the data.
        """
        file_path = os.path.join(self.data_dir, filename)
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return json.load(f)
        else:
            raise FileNotFoundError(f"{filename} not found in {self.data_dir}")

    def load_excel(self, filename: str, sheet_name: str = None) -> pd.DataFrame:
        """
        Load an Excel file into a DataFrame.
        :param filename: Name of the Excel file.
        :param sheet_name: Name of the sheet to load (default is the first sheet).
        :return: DataFrame containing the data.
        """
        file_path = os.path.join(self.data_dir, filename)
        if os.path.exists(file_path):
            return pd.read_excel(file_path, sheet_name=sheet_name)
        else:
            raise FileNotFoundError(f"{filename} not found in {self.data_dir}")

    def load_images(self, image_dir: str) -> List[str]:
        """
        Load image file paths from a directory.
        :param image_dir: Directory containing images.
        :return: List of image file paths.
        """
        image_paths = [os.path.join(image_dir, img) for img in os.listdir(image_dir) if img.endswith(('.png', '.jpg', '.jpeg'))]
        if not image_paths:
            raise FileNotFoundError(f"No images found in {image_dir}")
        return image_paths

    def load_data(self, filename: str, file_type: str = 'csv') -> Union[pd.DataFrame, Dict, List]:
        """
        Load data from various formats based on file extension.
        :param filename: Name of the file.
        :param file_type: Type of the file ('csv', 'json', 'excel').
        :return: DataFrame, dictionary, or list containing the data.
        """
        if file_type == 'csv':
            return self.load_csv(filename)
        elif file_type == 'json':
            return self.load_json(filename)
        elif file_type == 'excel':
            return self.load_excel(filename)
        else:
            raise ValueError("Unsupported file format. Please provide a CSV, JSON, or Excel file.")

    def validate_data(self, df: pd.DataFrame) -> Dict[str, Union[int, float]]:
        """
        Validate the DataFrame for missing values and duplicates.
        :param df: DataFrame to validate.
        :return: Dictionary with validation results.
        """
        missing_values = df.isnull().sum().sum()
        duplicate_rows = df.duplicated().sum()
        total_rows = df.shape[0]
        return {
            'total_rows': total_rows,
            'missing_values': missing_values,
            'duplicate_rows': duplicate_rows
        }

    def explore_data(self, df: pd.DataFrame) -> None:
        """
        Print basic statistics and information about the DataFrame.
        :param df: DataFrame to explore.
        """
        print("DataFrame Info:")
        print(df.info())
        print("\nBasic Statistics:")
        print(df.describe(include='all'))

# Example usage
if __name__ == "__main__":
    data_loader = DataLoader(data_dir='path/to/data')

    # Load a CSV file
    try:
        df = data_loader.load_data('data.csv', file_type='csv')
        print("CSV Data Loaded Successfully.")
    except Exception as e:
        print(e)

    # Validate the loaded data
 validation_results = data_loader.validate_data(df)
    print("Validation Results:")
    print(validation_results)

    # Explore the loaded data
    data_loader.explore_data(df)
