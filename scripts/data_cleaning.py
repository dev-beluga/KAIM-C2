import pandas as pd

def clean_data(df, timestamp_col):
    df = df.copy()  # Ensure df is a copy

    # Convert Timestamp column to datetime
    df[timestamp_col] = pd.to_datetime(df[timestamp_col])
    
    # Extract only the date part (year/month/day)
    df['Date'] = df[timestamp_col].dt.date
    
    # Drop the original Timestamp column
    df.drop(timestamp_col, axis=1, inplace=True)
    
    # Reorder columns to place 'Date' where 'Timestamp' was
    current_order = df.columns.tolist()
    new_order = ['Date'] + [col for col in current_order if col != 'Date']
    df = df[new_order]
    
    # Identify columns with null values
    null_columns = df.columns[df.isnull().any()].tolist()
    for col in null_columns:
        # Drop the column with null values
        df.drop(col, axis=1, inplace=True)

    return df

def replace_negative_values(df):
    # Select only numeric columns
    num_df = df.select_dtypes(include=['number']).copy()

    # Replace negative values with zero
    num_df[num_df < 0] = 0
    
    # Update the original DataFrame with the modified numeric values
    for col in num_df.columns:
        df[col] = num_df[col]
    
    return df
    
    return df
