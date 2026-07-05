# Regional Analysis: Top 5 states with highest average unemployment rates during the full period vs during COVID months (April-June 2020)
covid_df = df_clean[df_clean['Date'] >= '2020-04-01']
pre_covid_df = df_clean[df_clean['Date'] < '2020-04-01']

top_states_overall = df_clean.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values(ascending=False).head(5)
top_states_covid = covid_df.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values(ascending=False).head(5)

print("Top 5 states with highest average unemployment overall:")
print(top_states_overall)
print("\nTop 5 states with highest average unemployment during COVID lockdown (Apr-Jun 2020):")
print(top_states_covid)

# Let's do a correlation matrix between features
corr = df_clean[['Estimated Unemployment Rate (%)', 'Estimated Employed', 'Estimated Labour Participation Rate (%)']].corr()
print("\nCorrelation Matrix:")
print(corr)