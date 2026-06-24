# dashboard.py

import pandas as pd
import streamlit as st
import subprocess

st.set_page_config(layout="wide")

st.title("Apex Trend Scanner")
from datetime import datetime
from zoneinfo import ZoneInfo

ist_time = datetime.now(ZoneInfo("Asia/Kolkata"))

st.write(
    "Last Scan:",
    ist_time.strftime("%d-%m-%Y %H:%M:%S IST")
)

with st.spinner("Scanning Market..."):
    subprocess.run(["python", "scanner.py"])

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
