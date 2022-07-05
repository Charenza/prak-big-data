import yfinance as yf
import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta


st.write("""
# Aplikasi Yahoo Finance
## Data saham Google

Berikut ini adalah data Closing price dan volume dari Google.
""")

ticker = st.selectbox(
    "Ticker Perusahaan",
    options = ["ANTM", "BBNI", "JSMR", "TLK", "EXCL"]
)

tickerData = yf.Ticker(ticker)

jumlah_hari = timedelta(days=-30)
tgl_mulai = st.date_input(
    "Mulai dari tanggal",
    value=date.today()+jumlah_hari
)
tgl_akhir = st.date_input(
    "Hingga",
    value=date.today()
)
# hard coded
tickerDF = tickerData.history(
    period='Id', 
    start=str(tgl_mulai),
    end=str(tgl_akhir)
)

if ticker == 'ANTM':
    nama_perusahaan = "Aneka tambang"
elif ticker == 'BBNI':
    nama_perusahaan = "Bank Negara Indonesia"
elif ticker == 'JSMR':
    nama_perusahaan = "Jasamarga"
elif ticker == 'TLK':
    nama_perusahaan = "Telkom Indonesia"
elif ticker == 'EXCL':
    nama_perusahaan = "XL Axiata"
    
#f-string
st.markdown(f"Harga penutupan *(nama_perusahaan)*")
st.plotly_chart(
    px.line(tickerDF.Close)
)
st.line_chart(tickerDF.Close)

st.markdown(f"Volume transaksi saham *(nama_perusahaan)*")
st.plotly_chart(
    px.line(tickerDF.Volume)
)
st.line_chart(tickerDF.Volume)

st.markdown(f"Harga tertinggi *(nama_perusahaan)*")
st.plotly_chart(
    px.line(tickerDF.High)
)
st.line_chart(tickerDF.High)
