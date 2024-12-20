# FEMA Disaster Response Insights

## Overview
This project analyzes FEMA disaster response data to evaluate the effectiveness of Emergency Operations Centers (EOCs) and optimize their locations. By leveraging statistical analysis and data visualization, the project provides actionable insights to enhance national emergency response strategies. The accompanying Streamlit app enables stakeholders to explore these insights interactively.

## Problem Statement
Effective disaster response requires EOCs to be strategically located to minimize response time and distance. This project addresses the following key questions:

1. Are incident frequencies being sufficiently considered in EOC placement decisions?
2. Do EOCs demonstrate regional specialization for handling specific types of disasters?
3. Are travel times and overall response efficiency consistent across regions and disaster types?

## Objectives
- Analyze the relationship between incident types, disaster areas, and EOC locations.
- Provide national and state-level insights into response times, distances, and typical incidents.
- Build a Streamlit app to visualize findings and allow users to interact with the data.

## Dataset
The primary dataset used in this project is sourced from FEMA, containing detailed information on disaster declarations. Key features include:

- **Disaster Area Coordinates**: Latitude and longitude of disaster sites.
- **EOC Coordinates**: Locations of assigned Emergency Operations Centers.
- **Incident Type**: Classification of the disaster.
- **Distance and Duration**: Travel distance and time between disaster areas and EOCs.

### Data Cleaning and Preparation
The dataset underwent the following preprocessing steps:
- Removal of irrelevant columns.
- Handling missing values.
- Adding calculated features like travel distance and response time.

## Methodology

### 1. Exploratory Data Analysis (EDA)
- Statistical analysis of key metrics such as average response time and distance.
- Visualization of distributions and trends.

### 2. Hypothesis Testing
- Evaluated relationships between incident types and disaster areas.
- Assessed whether EOC locations align with response efficiency.

### 3. Streamlit Application
- Developed an interactive app to showcase project findings, including:
  - National and state-level metrics.
  - Visualizations of travel time and distance distributions.
  - Insights into the most typical incidents and most utilized EOCs.

## Key Performance Indicators (KPIs)
The project focuses on three primary KPIs:
1. **Incident Frequencies and EOC Placement**: Assessing whether EOC placement sufficiently accounts for incident frequencies.
2. **Regional Specialization of EOCs**: Evaluating if EOCs demonstrate specialization in handling specific types of disasters.
3. **Response Efficiency**: Analyzing consistency in travel times and response efficiency across regions and disaster types.

## Streamlit Application
The Streamlit app offers an interactive interface for users to explore the insights:
- **National Insights**: Average response time and distance across the United States.
- **State-Level Insights**: Metrics specific to selected states.
- **Visualizations**: Distributions of travel times and distances.

### How to Run the App
1. Clone this repository.
2. Install the required packages using `pip install streamlit pandas matplotlib seaborn`.
3. Run the app with `streamlit run main_streamlit.py`.
4. Open the provided URL in your browser.

## Tools and Technologies
- **Python**: Data analysis and preprocessing.
- **Pandas**: Data manipulation.
- **Seaborn & Matplotlib**: Data visualization.
- **Streamlit**: Interactive web application.
- **Google Maps API**: Used for obtaining coordinates.

## Results and Recommendations
- **Insights**: EOCs in some regions are sub-optimally located, leading to higher response times and distances.
- **Recommendations**:
  1. Reevaluate the placement of underperforming EOCs.
  2. Invest in additional resources for high-demand EOCs.
  3. Optimize routes using advanced tools for future disaster planning.

## Conclusion
This project demonstrates how data-driven insights can enhance disaster response strategies, ultimately saving lives and resources. By integrating statistical analysis and visualization, the project provides a comprehensive evaluation of EOC performance.

## Future Work
- Incorporate real-time data for dynamic analysis.
- Expand the scope to include additional datasets, such as resource allocation and vehicle tracking.
- Develop predictive models for future disaster planning.

## Author
**Marc Greenlee**

link to the presentation slides: https://www.canva.com/design/DAGZUqgKomc/zebf1SkElyYjHyUvKmqOkQ/edit
---

Thank you for exploring this project. Your feedback and suggestions are welcome!

