"""Data Visualization Showcase
Examples of effective visualizations for computational data science portfolios.
Useful for courses like CMSE 402 (Data Visualization).
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

np.random.seed(42)

# Sample dataset: Michigan weather-inspired or student metrics
dates = pd.date_range('2023-01-01', periods=365, freq='D')
weather = pd.DataFrame({
    'date': dates,
    'temp_f': 45 + 30*np.sin(2*np.pi*np.arange(365)/365) + np.random.normal(0, 5, 365),
    'precipitation': np.random.exponential(0.15, 365),
    'month': dates.month
})

# 1. Time series with matplotlib
plt.figure(figsize=(12, 5))
plt.plot(weather['date'], weather['temp_f'], color='steelblue', alpha=0.8)
plt.title('Daily Temperature Trends (Synthetic Michigan-inspired)')
plt.xlabel('Date')
plt.ylabel('Temperature (°F)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('temperature_timeseries.png', dpi=150)
plt.show()

# 2. Seaborn categorical / distribution
plt.figure(figsize=(10, 6))
sns.boxplot(data=weather, x='month', y='temp_f', palette='coolwarm')
plt.title('Temperature Distribution by Month')
plt.xlabel('Month')
plt.ylabel('Temperature (°F)')
plt.savefig('temp_by_month_boxplot.png', dpi=150)
plt.show()

# 3. Correlation / pair-style
corr_data = weather[['temp_f', 'precipitation']].copy()
corr_data['humidity_proxy'] = 50 + 20*np.sin(2*np.pi*np.arange(365)/365) + np.random.normal(0, 8, 365)
plt.figure(figsize=(8, 6))
sns.heatmap(corr_data.corr(), annot=True, cmap='RdBu_r', center=0)
plt.title('Correlation of Weather Variables')
plt.savefig('weather_correlation.png', dpi=150)
plt.show()

# 4. Interactive Plotly (if run in notebook or with display)
fig = px.line(weather, x='date', y='temp_f', title='Interactive Temperature Time Series',
              labels={'temp_f': 'Temp (°F)', 'date': 'Date'})
fig.add_scatter(x=weather['date'], y=weather['precipitation']*50, mode='lines',
                name='Precipitation (scaled)', yaxis='y2')
fig.update_layout(yaxis2=dict(overlaying='y', side='right', title='Precip'))
fig.write_html('interactive_weather.html')
print('Interactive plot saved as interactive_weather.html')

# 5. Bar chart of monthly averages
monthly = weather.groupby('month')['temp_f'].mean().reset_index()
plt.figure(figsize=(10, 5))
sns.barplot(data=monthly, x='month', y='temp_f', palette='viridis')
plt.title('Average Monthly Temperature')
plt.xlabel('Month')
plt.ylabel('Avg Temp (°F)')
plt.savefig('monthly_avg_temp.png', dpi=150)
plt.show()

print('\nVisualization examples generated. Check PNG files and HTML.')
