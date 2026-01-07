import pandas as pd

def load_data(filepath):
    """
    Loads complaint data from CSV file
    """
    try:
        df = pd.read_csv(filepath)
        return df
    except Exception as e:
        print("Error loading data:", e)
        return None
