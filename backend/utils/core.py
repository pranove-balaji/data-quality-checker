import pandas as pd

def data_checker(df):
    report=""
    #statistical data
    report+=f"total rows: {len(df)}\n"
    report+=f"total columns: {len(df.columns)}\n\n"
    #missing values
    missing_values=df.isnull().mean()*100
    report+="missing value (% per column):"
    report+=missing_values.to_string()
    report+="\n\n"
    #duplicate rows
    duplicate_rows=df.duplicated().sum()
    report+=f"duplicate rows: {duplicate_rows}\n\n"
    #datatypes
    data_types=df.dtypes.to_string()
    report+=f"data types: {data_types}\n\n"
    return report