import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data(1990) by Jngwen Qiu')
df = pd.read_csv('housing.csv')

houseprice_filter = st.slider(' Median House Price:', 0, 500001, 200000)

location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  
     df.ocean_proximity.unique())

income_filter = st.sidebar.radio(
    'Choose income level',
    ('Low','Medium','High')
)


df = df[df.ocean_proximity.isin(location_filter)]

if income_filter =='Low':
    df = df[df.median_income <= 2.5]
if income_filter == 'High':
    df = df[df.median_income > 4.5]
else:
    income_filter == 'Medium'


df  = df[df.median_house_value >= houseprice_filter]
st.map(df)


st.subheader('Histogram Of the Median House Value')

fig, ax = plt.subplots(figsize=(20, 5))
df.median_house_value.hist(ax=ax,bins = 30)
st.pyplot(fig)