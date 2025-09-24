import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def basic_statistics(df: pd.DataFrame):
    """Gera estatísticas básicas para cada coluna"""
    stats = {}
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            stats[col] = {
                "mean": df[col].mean(),
                "median": df[col].median(),
                "mode": df[col].mode().tolist(),
                "std": df[col].std(),
                "min": df[col].min(),
                "max": df[col].max(),
                "unique": df[col].nunique(dropna=False),
                "nulls": df[col].isnull().sum(),
                "duplicates": df[col].duplicated().sum()
            }
        else:
            stats[col] = {
                "unique": df[col].nunique(),
                "top_values": df[col].value_counts().head(5).to_dict(),
                "nulls": df[col].isnull().sum(),
                "duplicates": df[col].duplicated().sum()
            }
    return stats


