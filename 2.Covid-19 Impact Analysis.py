# Let's fix the warning and show the output properly
df_clean = df.dropna(subset=['Region', 'Date']).copy()
df_clean.columns = df_clean.columns.str.strip()
df_clean['Date'] = pd.to_datetime(df_clean['Date'].str.strip(), format='%d-%m-%Y')
df_clean['Year'] = df_clean['Date'].dt.year
df_clean['Month'] = df_clean['Date'].dt.month

print("Date range in dataset:", df_clean['Date'].min(), "to", df_clean['Date'].max())
print("\nSummary Statistics for Unemployment Rate:")
print(df_clean['Estimated Unemployment Rate (%)'].describe())