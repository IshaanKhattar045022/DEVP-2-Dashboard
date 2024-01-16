#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import streamlit as st
import plotly.express as px
import random

# Function to find an available port (not needed for Streamlit)
def find_open_port():
    return 8501  # Streamlit runs on port 8501 by default

# Assuming you have loaded your data into a DataFrame called 'df'
file_path = r'telecom_churn.csv'
df = pd.read_csv(file_path)

# Sidebar with the state dropdown
selected_state = st.sidebar.selectbox('Select a state', df['State'].unique(), index=0)

# Filter the DataFrame based on the selected state
filtered_df = df[df['State'] == selected_state]

# Display the title
st.title("Telecom Customer Analysis")

# Bar chart
st.plotly_chart(px.bar(filtered_df, x='Customer service calls', y='Total day minutes', title='Customer Analysis', color='Churn'))

# Scatter plot
st.plotly_chart(px.scatter(filtered_df, x='Account length', y='Total day minutes', title='Account Length vs Day Minutes', color='Churn'))

# Pie chart
st.plotly_chart(px.pie(filtered_df, names='Churn', title='Churn Distribution'))

# Line chart
st.plotly_chart(px.line(filtered_df, x='Total day charge', y='Total night minutes', title='Day Charge vs Night Minutes', color='Churn'))

# Box plot
st.plotly_chart(px.box(filtered_df, x='Churn', y='Total day minutes', title='Box Plot of Day Minutes by Churn Status'))

# Bubble chart
st.plotly_chart(px.scatter(filtered_df, x='Customer service calls', y='Total day minutes', title='Bubble Chart', color='Churn', size='Total eve minutes'))

# Histogram
st.plotly_chart(px.histogram(filtered_df, x='Total day charge', nbins=20, title='Distribution of Day Charge'))

# Donut chart
st.plotly_chart(px.pie(filtered_df, names='Churn', hole=0.4, title='Churn Distribution (Donut Chart)'))

# Area chart
st.plotly_chart(px.area(filtered_df, x='Customer service calls', y='Total night minutes', title='Area Chart: Night Minutes vs Service Calls', color='Churn'))


# In[ ]:





