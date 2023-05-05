import pandas as pd
# Load the dataset from the previous problem
df = pd.read_csv('data.csv')

# Sort the dataframe by Date
df = df.sort_values('Date')

# Calculate the 30-day moving average of trading volume for each stock and ETF
df['vol_moving_avg'] = df.groupby('Symbol')['Volume'].rolling(window=30).mean().reset_index(drop=True)

# Calculate the rolling median of the adjusted closing price
df['adj_close_rolling_med'] = df.groupby('Symbol')['Adj Close'].rolling(window=30).median().reset_index(level=0, drop=True)

# Save the resulting dataset to a new Parquet file
df.to_csv('new_dataset.csv')
