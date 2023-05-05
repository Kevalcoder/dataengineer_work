import os
import pandas as pd


# Define the path to the Stocks folder
etfs_folder = "etfs"
stocks_folder = "stocks"
symbols_file = pd.read_csv("symbols_valid_meta.csv")

df_list1 = []
df_list2 = []

# Load each CSV file into a list
for file_name in os.listdir(etfs_folder):
    if file_name.endswith('.csv'):
        file_path = os.path.join(etfs_folder, file_name)
        df = pd.read_csv(file_path)
        df_list1.append(df)

for file_name in os.listdir(stocks_folder):
    if file_name.endswith('.csv'):
        file_path = os.path.join(stocks_folder, file_name)
        df = pd.read_csv(file_path)
        df_list2.append(df)

# convert list to DataFrame
folder1_df = pd.concat(df_list1)
folder2_df = pd.concat(df_list2)
concatenated_df = pd.concat([folder1_df, folder2_df])



# Concatenate the two dataframes
final_df = pd.concat([concatenated_df, symbols_file], axis = 1)

final_data = final_df[['Symbol', 'Security Name', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]



# Print the combined dataframe
final_data.to_parquet('data.parquet')





