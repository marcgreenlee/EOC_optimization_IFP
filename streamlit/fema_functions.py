
import pandas as pd

def calculate_avg_distance(df):
    try:
        # Calculate national averages
        avg_distance_national = df['Distance (km)'].mean() if 'Distance (km)' in df.columns else None
        avg_travel_time_national = df['Duration (minutes)'].mean() if 'Duration (minutes)' in df.columns else None
        
        # Calculate state averages
        avg_distance_state = df.groupby('state')['Distance (km)'].mean() if 'Distance (km)' in df.columns else pd.Series()
        avg_travel_time_state = df.groupby('state')['Duration (minutes)'].mean() if 'Duration (minutes)' in df.columns else pd.Series()
        
        return avg_distance_national, avg_travel_time_national, avg_distance_state, avg_travel_time_state
    except Exception as e:
        print(f"Error in calculate_avg_distance: {e}")
        return None, None, None, None

def most_typical_incident(df):
    # National-level most typical incident (string)
    most_typical_national = df['incidentType'].mode()[0] if not df['incidentType'].mode().empty else None
    
    # State-level most typical incident (pandas Series)
    most_typical_state = df.groupby('state')['incidentType'].agg(lambda x: x.mode()[0] if not x.mode().empty else None)
    
    return most_typical_national, most_typical_state


def most_utilized_hubs(df):
    # National-level most utilized EOC (string)
    most_utilized_national = df['EOC'].mode()[0] if not df['EOC'].mode().empty else None
    
    # State-level most utilized EOC (pandas Series)
    most_utilized_state = df.groupby('state')['EOC'].agg(lambda x: x.mode()[0] if not x.mode().empty else None)
    
    return most_utilized_national, most_utilized_state 