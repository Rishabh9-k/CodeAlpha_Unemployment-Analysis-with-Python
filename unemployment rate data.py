import pandas as pd
import os

# Check if the file exists and its location
file_name = "Unemployment in India.csv"
if os.path.exists(file_name):
    print("File exists")
    df = pd.read_csv(file_name)
    print(df.info())
    print(df.head())
else:
    print("File not found")