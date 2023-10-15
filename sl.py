import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Create a Streamlit web app
st.title('Interactive Line Chart')

# Generate some example data
data = pd.DataFrame({
    'x': np.arange(0, 10, 0.1),
    'y': np.sin(np.arange(0, 10, 0.1))
})

# Sidebar for user input
st.sidebar.header('Chart Settings')
selected_range = st.sidebar.slider('Select a range', 0.0, 10.0, (2.0, 8.0))
filtered_data = data[(data['x'] >= selected_range[0]) & (data['x'] <= selected_range[1])]

# Create an interactive line chart
st.altair_chart(alt.Chart(filtered_data).mark_line().encode(x='x', y='y'), use_container_width=True)

