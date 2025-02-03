import streamlit as st
import requests

st.set_page_config(
    page_title = "Rainfall-prediction",
    page_icon = "image.png",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Streamlit UI
st.title("🌧️ Rainfall Prediction App")

st.markdown("Enter the weather parameters below and click **Predict** to see the result.")

# User inputs
pressure = st.number_input("Pressure (hPa)", min_value=900.0, max_value=1100.0, step=0.1, value=None)
dewpoint = st.number_input("Dew Point (°C)", min_value=-10.0, max_value=30.0, step=0.1, value=None)
humidity = st.number_input("Humidity (%)", min_value=0, max_value=100, step=1, value=None)
cloud = st.number_input("Cloud Cover (%)", min_value=0, max_value=100, step=1, value=None)
sunshine = st.number_input("Sunshine Hours", min_value=0.0, max_value=15.0, step=0.1, value=None)
winddirection = st.number_input("Wind Direction (°)", min_value=0, max_value=360, step=1, value=None)
windspeed = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=100.0, step=0.1, value=None)

# Prediction button
if st.button("Predict"):
    input_data = {
        "pressure": pressure,
        "dewpoint": dewpoint,
        "humidity": humidity,
        "cloud": cloud,
        "sunshine": sunshine,
        "winddirection": winddirection,
        "windspeed": windspeed
    }

    # Send data to Flask API
    try:
        response = requests.post("http://localhost:5000/predict", json=input_data)
        result = response.json()

        if "prediction" in result:
            prediction = "🌧️ Rainfall" if result["prediction"] == 1 else "☀️ No Rainfall"
            st.success(f"Prediction: **{prediction}**")
        else:
            st.error("Error: Unable to get prediction.")
    except requests.exceptions.ConnectionError:
        st.error("Error: Unable to connect to the backend. Ensure Flask server is running.")
