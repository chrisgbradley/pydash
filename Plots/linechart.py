import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Creating sum of number of cases group by Country Column
max_df = df.groupby(['month']).agg(
    {'actual_max_temp': 'max'}).reset_index()

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
max_df['month'] = pd.Categorical(max_df['month'], categories=months, ordered=True)
max_df.sort_values(by=['month'], inplace=True)

# Preparing data
data = [go.Scatter(x=max_df['month'], y=max_df['actual_max_temp'], mode='lines', name='Temperature')]

# Preparing layout
layout = go.Layout(title='Actual Max Temperature per month for 2014 - 2015', xaxis_title="Month & Year",
                   yaxis_title="Actual Max Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechart.html')