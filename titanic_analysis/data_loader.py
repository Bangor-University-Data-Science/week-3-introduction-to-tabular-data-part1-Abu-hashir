# titanic_analysis/data_loader.py
import pandas as pd

def load_titanic_data(filepath: str) -> pd.DataFrame:
    """Loads the Titanic dataset from a CSV file."""
    df = pd.read_csv('data/titanic.csv')
    return df
