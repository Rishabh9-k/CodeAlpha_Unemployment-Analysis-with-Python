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


Code output
Top 5 states with highest average unemployment overall:
Region
Tripura             28.350357
Haryana             26.283214
Jharkhand           20.585000
Bihar               18.918214
Himachal Pradesh    18.540357
Name: Estimated Unemployment Rate (%), dtype: float64

Top 5 states with highest average unemployment during COVID lockdown (Apr-Jun 2020):
Region
Puducherry    57.700000
Jharkhand     44.896667
Haryana       37.693333
Bihar         36.988333
Tamil Nadu    31.735000
Name: Estimated Unemployment Rate (%), dtype: float64

Correlation Matrix:
                                         Estimated Unemployment Rate (%)  Estimated Employed  Estimated Labour Participation Rate (%)
Estimated Unemployment Rate (%)                                 1.000000           -0.222876                                 0.002558
Estimated Employed                                             -0.222876            1.000000                                 0.011300
Estimated Labour Participation Rate (%)                         0.002558            0.011300                                 1.000000
