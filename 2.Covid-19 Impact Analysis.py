# Let's fix the warning and show the output properly
df_clean = df.dropna(subset=['Region', 'Date']).copy()
df_clean.columns = df_clean.columns.str.strip()
df_clean['Date'] = pd.to_datetime(df_clean['Date'].str.strip(), format='%d-%m-%Y')
df_clean['Year'] = df_clean['Date'].dt.year
df_clean['Month'] = df_clean['Date'].dt.month

print("Date range in dataset:", df_clean['Date'].min(), "to", df_clean['Date'].max())
print("\nSummary Statistics for Unemployment Rate:")
print(df_clean['Estimated Unemployment Rate (%)'].describe())


Code output
Date range in dataset: 2019-05-31 00:00:00 to 2020-06-30 00:00:00

Summary Statistics for Unemployment Rate:
count    740.000000
mean      11.787946
std       10.721298
min        0.000000
25%        4.657500
50%        8.350000
75%       15.887500
max       76.740000
Name: Estimated Unemployment Rate (%), dtype: float64
