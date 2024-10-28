# data/data_visualization.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from typing import List, Dict, Any

class DataVisualizer:
    def __init__(self, df: pd.DataFrame):
        """
        Initialize the DataVisualizer with a DataFrame.
        :param df: DataFrame to visualize.
        """
        self.df = df

    def plot_distribution(self, column: str, bins: int = 30, kde: bool = True) -> None:
        """
        Plot the distribution of a specified column.
        :param column: Column name to visualize.
        :param bins: Number of bins for the histogram.
        :param kde: Whether to include a Kernel Density Estimate (KDE) plot.
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(self.df[column], bins=bins, kde=kde)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.grid()
        plt.show()

    def plot_boxplot(self, column: str) -> None:
        """
        Plot a boxplot for a specified column.
        :param column: Column name to visualize.
        """
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=self.df[column])
        plt.title(f'Boxplot of {column}')
        plt.xlabel(column)
        plt.grid()
        plt.show()

    def plot_correlation_matrix(self) -> None:
        """
        Plot the correlation matrix of the DataFrame.
        """
        plt.figure(figsize=(12, 8))
        correlation = self.df.corr()
        sns.heatmap(correlation, annot=True, fmt=".2f", cmap='coolwarm', square=True)
        plt.title('Correlation Matrix')
        plt.show()

    def plot_pairplot(self, hue: str = None) -> None:
        """
        Plot pairwise relationships in the dataset.
        :param hue: Column name for color encoding.
        """
        sns.pairplot(self.df, hue=hue)
        plt.title('Pairplot of the DataFrame')
        plt.show()

    def plot_time_series(self, time_column: str, value_column: str) -> None:
        """
        Plot a time series for a specified time and value column.
        :param time_column: Column name for time.
        :param value_column: Column name for values.
        """
        plt.figure(figsize=(14, 7))
        plt.plot(self.df[time_column], self.df[value_column], marker='o')
        plt.title(f'Time Series of {value_column} over {time_column}')
        plt.xlabel(time_column)
        plt.ylabel(value_column)
        plt.grid()
        plt.show()

    def plot_category_counts(self, column: str) -> None:
        """
        Plot counts of categories in a specified column.
        :param column: Column name to visualize.
        """
        plt.figure(figsize=(12, 6))
        sns.countplot(data=self.df, x=column, order=self.df[column].value_counts().index)
        plt.title(f'Count of Categories in {column}')
        plt.xticks(rotation=45)
        plt.grid()
        plt.show()

    def save_plot(self, filename: str) -> None:
        """
        Save the current plot to a file.
        :param filename: Name of the file to save the plot.
        """
        plt.savefig(filename)
        plt.close()

    def visualize_all(self, columns: List[str]) -> None:
        """
        Visualize distributions and boxplots for a list of columns.
        :param columns: List of column names to visualize.
        """
        for column in columns:
            self.plot_distribution(column)
            self.plot_boxplot(column)

# Example usage
if __name__ == "__main__":
    # Load data
    data_loader = DataLoader(data_dir='path/to/data')
    df = data_loader.load_data('data.csv', file_type='csv')

    # Visualize data
    visualizer = DataVisualizer(df)
    visualizer.plot_distribution('numerical_column')
    visualizer.plot_boxplot('numerical_column')
    visualizer.plot_correlation_matrix()
    visualizer.plot_pairplot(hue='target_column')
    visualizer.plot_time_series(time_column='date_column', value_column='value_column')
    visualizer.plot_category_counts(column='category_column')
