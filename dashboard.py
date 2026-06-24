# dashboard.py

import pandas as pd
import streamlit as st
import subprocess
from streamlit_autorefresh import st_autorefresh

st.set_page_config(layout="wide")

st.title("Apex Trend Scanner")

# Auto refresh every 5 minutes
st_autorefresh(
    interval=300000,  # 300 seconds = 5 minutes
    key="scanner_refresh"
)

from datetime import datetime
from zoneinfo import ZoneInfo

ist_time = datetime.now(ZoneInfo("Asia/Kolkata"))

market_open = (
    (ist_time.hour > 9 or (ist_time.hour == 9 and ist_time.minute >= 15))
    and
    (ist_time.hour < 15 or (ist_time.hour == 15 and ist_time.minute <= 30))
)

if market_open:
    with st.spinner("Scanning Market..."):
        subprocess.run(["python", "scanner.py"])

with st.spinner("Scanning Market..."):
    result = subprocess.run(
        ["python", "scanner.py"],
        capture_output=True,
        text=True
    )

df = pd.read_csv("output.csv")

bull = df[df["Direction"] == "BULL"]
bear = df[df["Direction"] == "BEAR"]
sideways = df[df["Direction"] == "SIDEWAYS"]

st.subheader("Bullish Stocks")
st.dataframe(bull)

st.subheader("Bearish Stocks")
st.dataframe(bear)

st.subheader("Sideways Stocks")
st.dataframe(sideways)
