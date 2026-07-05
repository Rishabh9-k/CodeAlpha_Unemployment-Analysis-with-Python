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