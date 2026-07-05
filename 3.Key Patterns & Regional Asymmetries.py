import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_theme(style="whitegrid")

# 1. Overall Unemployment Trend over time (monthly average)
monthly_trend = df_clean.groupby('Date')['Estimated Unemployment Rate (%)'].mean().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_trend, x='Date', y='Estimated Unemployment Rate (%)', marker='o', color='crimson', linewidth=2.5)
plt.title('Average Unemployment Rate Trend in India (May 2019 - June 2020)', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Average Unemployment Rate (%)', fontsize=12)
plt.axvline(pd.to_datetime('2020-03-24'), color='black', linestyle='--', label='COVID-19 National Lockdown Start')
plt.legend()
plt.tight_layout()
plt.savefig('unemployment_trend.png')
plt.close()

# 2. Impact by Area (Rural vs Urban)
area_trend = df_clean.groupby(['Date', 'Area'])['Estimated Unemployment Rate (%)'].mean().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(data=area_trend, x='Date', y='Estimated Unemployment Rate (%)', hue='Area', marker='o', palette='Set1', linewidth=2.5)
plt.title('Rural vs Urban Unemployment Rate Trends', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Average Unemployment Rate (%)', fontsize=12)
plt.axvline(pd.to_datetime('2020-03-24'), color='black', linestyle='--')
plt.tight_layout()
plt.savefig('rural_vs_urban.png')
plt.close()

print("Trend files saved.")



Code output

Trend files saved.
