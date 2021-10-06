import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Aggregate Max, Min, Mean temps by Month
new_df = df.groupby(['month']).agg(
    {'average_max_temp': 'mean', 'average_min_temp': 'mean'}).reset_index()

# Preparing data
data = [
    go.Scatter(y=new_df['average_max_temp'],
               x=new_df['average_min_temp'],
               text=new_df['month'],
               mode='markers',
               marker=dict(size=new_df['average_max_temp'],color=new_df['average_max_temp'], showscale=True))]

# Preparing layout
layout = go.Layout(title='Average Min/Max Temperatures 2014-2015', yaxis_title="Average Max Temp",
                   xaxis_title="Average Min Temp", hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart.html')