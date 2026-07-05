# Let's clean the data: remove whitespaces from columns, handle null values, and convert date column to datetime.
# Print column names exactly
print("Original Columns:", df.columns.tolist())

# Strip spaces from column names
df.columns = df.columns.str.strip()
print("Cleaned Columns:", df.columns.tolist())

# Check for null values
print("\nNull values before cleaning:")
print(df.isnull().sum())

# Drop completely empty or mostly null rows (since 768 total but only 740 non-null)
df_clean = df.dropna(subset=['Region', 'Date'])

print("\nNull values after dropping rows:")
print(df_clean.isnull().sum())

# Clean the 'Date' column and convert to datetime
df_clean['Date'] = df_clean['Date'].str.strip()
df_clean['Date'] = pd.to_datetime(df_clean['Date'], format='%d-%m-%Y')

# Extract Month and Year for easier analysis
df_clean['Year'] = df_clean['Date'].dt.year
df_clean['Month'] = df_clean['Date'].dt.month

print("\nData overview after cleaning:")
print(df_clean.head())
print("Unique Years:", df_clean['Year'].unique())


Code output:

Original Columns: ['Region', ' Date', ' Frequency', ' Estimated Unemployment Rate (%)', ' Estimated Employed', ' Estimated Labour Participation Rate (%)', 'Area']
Cleaned Columns: ['Region', 'Date', 'Frequency', 'Estimated Unemployment Rate (%)', 'Estimated Employed', 'Estimated Labour Participation Rate (%)', 'Area']

Null values before cleaning:
Region                                     28
Date                                       28
Frequency                                  28
Estimated Unemployment Rate (%)            28
Estimated Employed                         28
Estimated Labour Participation Rate (%)    28
Area                                       28
dtype: int64

Null values after dropping rows:
Region                                     0
Date                                       0
Frequency                                  0
Estimated Unemployment Rate (%)            0
Estimated Employed                         0
Estimated Labour Participation Rate (%)    0
Area                                       0
dtype: int64

Data overview after cleaning:
           Region       Date Frequency  Estimated Unemployment Rate (%)  Estimated Employed  Estimated Labour Participation Rate (%)   Area  Year  Month
0  Andhra Pradesh 2019-05-31   Monthly                             3.65          11999139.0                                    43.24  Rural  2019      5
1  Andhra Pradesh 2019-06-30   Monthly                             3.05          11755881.0                                    42.05  Rural  2019      6
2  Andhra Pradesh 2019-07-31   Monthly                             3.75          12086707.0                                    43.50  Rural  2019      7
3  Andhra Pradesh 2019-08-31   Monthly                             3.32          12285693.0                                    43.97  Rural  2019      8
4  Andhra Pradesh 2019-09-30   Monthly                             5.17          12256762.0                                    44.68  Rural  2019      9
Unique Years: [2019 2020]
