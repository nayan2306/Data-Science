import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price APP

Shown are the stock **closing price** and **volume** of Google !
""")

#define the ticker symbol

tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d',start='2012-5-31',end='2022-5-31')

#open high low close  volume Dividends stock splits

st.write("""
## closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)