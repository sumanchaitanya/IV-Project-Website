import pandas as pd
import plotly.express as px
import streamlit as st

# Set page title and icon, and set layout to wide
st.set_page_config(page_title="EV Payments Dashboard", page_icon=":electric_plug:", layout="wide")

# Load data from Excel file
df = pd.read_excel(io='Book.xlsx', engine='openpyxl', sheet_name='Sheet1', nrows=42)

# Set up sidebar for filtering
st.sidebar.header("Please Filter Here:")

city = st.sidebar.multiselect("Select the City:", options=df["City"].unique(), default=df["City"].unique())
gender = st.sidebar.multiselect("Select the Gender:", options=df["Gender"].unique(), default=df["Gender"].unique())
dateofbirth = st.sidebar.multiselect("Select the Date of Birth:", options=df["Date of Birth"].unique(), default=df["Date of Birth"].unique())

# Filter data based on sidebar selections
df_selection = df.loc[(df["City"].isin(city)) & (df["Gender"].isin(gender)) & (df["Date of Birth"].isin(dateofbirth)), :]

# Set up main dashboard
st.title("EV Payments Dashboard")
st.subheader("Summary")

# Display filtered data summary
if df_selection.empty:
    st.warning("No data available for the selected filters.")
else:
    # Calculate and display age group with the most users
    age_counts = df_selection["Age"].value_counts()
    max_age = age_counts.index[0]
    st.write("The most common age group is:", max_age)

    # Calculate and display gender with the most users
    gender_counts = df_selection["Gender"].value_counts()
    max_gender = gender_counts.index[0]
    st.write("The most common gender is:", max_gender)

    # Calculate and display city with the most users
    city_counts = df_selection["City"].value_counts()
    max_city = city_counts.index[0]
    st.write("The city with the most users is:", max_city)

    # Display filtered data in table
    st.subheader("Filtered Data")
    st.dataframe(df_selection)

    # Create pie chart for age distribution
    st.subheader("Age Distribution")
    age_pie = px.pie(df_selection, names='Age')
    st.plotly_chart(age_pie)

    # Create pie chart for gender distribution
    st.subheader("Gender Distribution")
    gender_pie = px.pie(df_selection, names='Gender')
    st.plotly_chart(gender_pie)

    # Create pie chart for city distribution
    st.subheader("City Distribution")
    city_pie = px.pie(df_selection, names='City')
    st.plotly_chart(city_pie)
