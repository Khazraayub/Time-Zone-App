import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# ----------- Custom CSS for background and styling -------------
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #e0f7fa, #fff3e0);
    }
    .stApp {
        background: linear-gradient(to right, #e3ffe7, #d9e7ff);
    }
    h1, h3 {
        color: #2c3e50;
    }
    .stButton>button {
        background-color: #008CBA;
        color: white;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #005f73;
    }
    </style>
""", unsafe_allow_html=True)

# ----------- App Starts -------------
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_york",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",  
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

st.title("🌍 Time Zone App By Khazra Shaikh! ⏰")

selected_timezone = st.multiselect("Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"])

st.subheader("🕓 Selected Timezones")
for tz in selected_timezone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"**{tz}**: {current_time}")

st.subheader("🔄 Convert Time Between Timezones")

current_time = st.time_input("Current Time", value=datetime.now().time())

from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)
to_tz = st.selectbox("To TimeZone", TIME_ZONES, index=1)

if st.button("Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.success(f"✅ Converted Time in {to_tz}: {converted_time}")
