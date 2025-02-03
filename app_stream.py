import streamlit as st
import requests
import time

# Configure Streamlit page
st.set_page_config(
    page_title="🌦️ Rainfall Prediction",
    page_icon="🌧️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better UI
st.markdown("""
    <style>
        .main { background-color: #f5f7fa; }
        .stButton>button { 
            background-color: #4CAF50; color: white; font-size: 18px; border-radius: 10px; padding: 10px;
        }
        .stButton>button:hover { background-color: #45a049; }
        .prediction-result {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            padding: 10px;
            border-radius: 10px;
        }
        .rainy { background-color: #6fa3ef; color: white; }
        .sunny { background-color: #f7c948; color: black; }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.markdown("<h1 style='text-align: center;'>🌧️ Rainfall Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter the weather details below and click Predict to see if it will rain!</p>", unsafe_allow_html=True)

# Single column input layout
pressure = st.number_input("🔵 Pressure (hPa)", min_value=900.0, max_value=1100.0, step=0.1, value=1013.0)
dewpoint = st.number_input("🌡️ Dew Point (°C)", min_value=-10.0, max_value=30.0, step=0.1, value=10.0)
humidity = st.number_input("💧 Humidity (%)", min_value=0, max_value=100, step=1, value=70)
cloud = st.number_input("☁️ Cloud Cover (%)", min_value=0, max_value=100, step=1, value=50)
sunshine = st.number_input("☀️ Sunshine Hours", min_value=0.0, max_value=15.0, step=0.1, value=5.0)
winddirection = st.number_input("🧭 Wind Direction (°)", min_value=0, max_value=360, step=1, value=180)
windspeed = st.number_input("🌬️ Wind Speed (km/h)", min_value=0.0, max_value=100.0, step=0.1, value=10.0)

# Predict button
if st.button("🔮 Predict"):
    input_data = {
        "pressure": pressure,
        "dewpoint": dewpoint,
        "humidity": humidity,
        "cloud": cloud,
        "sunshine": sunshine,
        "winddirection": winddirection,
        "windspeed": windspeed
    }

    # Show loading animation
    with st.spinner("🔄 Fetching prediction..."):
        time.sleep(2)  # Simulating processing delay

        try:
            response = requests.post("http://localhost:5000/predict", json=input_data)
            result = response.json()

            if "prediction" in result:
                prediction = "🌧️ Rainfall" if result["prediction"] == 1 else "☀️ No Rainfall"
                color_class = "rainy" if result["prediction"] == 1 else "sunny"

                st.markdown(f'<p class="prediction-result {color_class}">{prediction}</p>', unsafe_allow_html=True)
            else:
                st.error("⚠️ Error: Unable to get prediction. Try again!")
        except requests.exceptions.ConnectionError:
            st.error("❌ Unable to connect to the backend. Ensure Flask server is running.")
