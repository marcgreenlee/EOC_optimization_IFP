import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fema_functions import (
    calculate_avg_distance,
    most_typical_incident,
    most_utilized_hubs
)

# Load Data
fema_df = pd.read_csv('/Users/marcgreenlee/Desktop/Ironhack/ironhack_projects/final_project/data/clean/fema_df_coords.csv')

# Streamlit App Setup
st.set_page_config(
    page_title="FEMA Disaster Response Insights",
    page_icon="🌎",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Title Section
st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="color: #4CAF50;">FEMA Disaster Response Insights</h1>
        <p style="font-size: 18px; color: gray;">Optimizing Emergency Operations Centers and Disaster Responses</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

# National Insights Section
st.subheader("National Insights")
avg_distance_national, avg_travel_time_national, _, _ = calculate_avg_distance(fema_df)

# Display National Metrics
col1, col2 = st.columns(2)
with col1:
    st.metric(
        label="Average Response Time (National)",
        value=f"{avg_travel_time_national:.2f} minutes" if avg_travel_time_national is not None else "Data unavailable",
    )
with col2:
    st.metric(
        label="Average Distance to Disaster (National)",
        value=f"{avg_distance_national:.2f} km" if avg_distance_national is not None else "Data unavailable",
    )

st.markdown("---")

# State-Level Insights Section
st.subheader("State-Level Insights")
state = st.selectbox(
    "Select a state:", fema_df["state"].unique(), key="state_selector"
)

# Get state-level data
avg_distance_state = calculate_avg_distance(fema_df)[2].get(state, "Data unavailable")
avg_travel_time_state = calculate_avg_distance(fema_df)[3].get(state, "Data unavailable")

# Get the most typical incident and most utilized EOC for the selected state
most_typical_incident_state = most_typical_incident(fema_df)[1].get(state, "Data unavailable")
most_utilized_eoc_state = most_utilized_hubs(fema_df)[1].get(state, "Data unavailable")

# Display State Metrics
col3, col4 = st.columns(2)
with col3:
    st.metric(
        label=f"Average Response Time ({state})",
        value=f"{avg_travel_time_state:.2f} minutes" if isinstance(avg_travel_time_state, (int, float)) else avg_travel_time_state,
    )
with col4:
    st.metric(
        label=f"Average Distance to Disaster ({state})",
        value=f"{avg_distance_state:.2f} km" if isinstance(avg_distance_state, (int, float)) else avg_distance_state,
    )

st.write(f"**Most Typical Incident in {state}:** {most_typical_incident_state}")
st.write(f"**Most Utilized EOC in {state}:** {most_utilized_eoc_state}")

st.markdown("---")

# Visualizations Section
st.subheader("Visualizations")

col5, col6 = st.columns(2)
with col5:
    st.write("Travel Time Distribution")
    fig, ax = plt.subplots()
    sns.histplot(fema_df["Duration (minutes)"], kde=True, ax=ax, color="skyblue")
    ax.set_title("Distribution of Travel Times")
    st.pyplot(fig)

with col6:
    st.write("Distance Distribution")
    fig, ax = plt.subplots()
    sns.histplot(fema_df["Distance (km)"], kde=True, ax=ax, color="orange")
    ax.set_title("Distribution of Distances")
    st.pyplot(fig)

# Footer Section
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center;">
        <p style="font-size: 14px; color: gray;">Created with Streamlit • Data Source: FEMA</p>
    </div>
    """,
    unsafe_allow_html=True,
)
