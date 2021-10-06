import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

# Get Top 20 by Total
top_20 = df.nlargest(20, 'Total')

# Format data
fig = px.bar(top_20, x='NOC', y='Total', title="Rio 2016 Olympic Games Medals")

# Preparing layout
layout = go.Layout(title='Rio 2016 Olympic Games Medals', xaxis_title="Nations",
                   yaxis_title="Number of Medals")

# Plot the figure and saving in a html file
pyo.plot(fig, filename='barchart.html')
