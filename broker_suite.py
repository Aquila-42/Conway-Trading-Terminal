
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime

def run_ultimate_broker_suite():
    print("'"*100)
    print("💎 CONWAYS CONSULTANCY: ULTIMATE REAL-TIME QUANT SUITE 💎")
    print(f"    Market Session: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("."*100)
    
    ticker = input("\nEnter Stock Symbol (e.g., AAPL, RELIANCE.NS): ").upper().strip()
    cur = "₹" if ".NS" in ticker or ".BO" in ticker else "$"
    
    # 1. DATA FETCHING
    df = yf.download(ticker, period="5d", interval="1m", progress=False)
    if df.empty: return print(f"❌ Error: Symbol '{ticker}' not found.")
    if isinstance(df.columns, pd.MultiIndex): df.columns = [col[0] for col in df.columns.values]

    # 2. INDICATOR ENGINEERING
    # Moving Average (9-period)
    df['MA9'] = df['Close'].rolling(window=9).mean()

    # Bollinger Bands (20-period, 2 Std Dev)
    df['BB_Mid'] = df['Close'].rolling(window=20).mean()
    df['BB_Std'] = df['Close'].rolling(window=20).std()
    df['BB_Upper'] = df['BB_Mid'] + (df['BB_Std'] * 2)
    df['BB_Lower'] = df['BB_Mid'] - (df['BB_Std'] * 2)

    # Wilder’s RSI
    window = 14
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0))
    loss = (-delta.where(delta < 0, 0))
    avg_gain = gain.ewm(alpha=1/window, min_periods=window, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1/window, min_periods=window, adjust=False).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan) 
    df['RSI'] = 100 - (100 / (1 + rs))
    
    # Volume Coloring Logic
    df['Vol_Color'] = np.where(df['Close'] >= df['Open'], '#3dc985', '#ef4f60')
    df['Time_Str'] = df.index.strftime('%Y-%m-%d %H:%M')
    df.dropna(inplace=True)

    # 3. 3-PANEL INTERACTIVE DASHBOARD
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, 
                        vertical_spacing=0.04, row_heights=[0.5, 0.2, 0.3],
                        subplot_titles=(f'{ticker} Price + Bollinger', 'RSI (Momentum)', 'Volume'))

    # PANEL 1: Price + BB + MA
    fig.add_trace(go.Candlestick(x=df['Time_Str'], open=df['Open'], high=df['High'], 
                                 low=df['Low'], close=df['Close'], name='Price'), row=1, col=1)
    # Bollinger Bands
    fig.add_trace(go.Scatter(x=df['Time_Str'], y=df['BB_Upper'], line=dict(color='rgba(173, 216, 230, 0.2)'), name='BB Upper'), row=1, col=1)
    fig.add_trace(go.Scatter(x=df['Time_Str'], y=df['BB_Lower'], line=dict(color='rgba(173, 216, 230, 0.2)'), 
                             fill='tonexty', fillcolor='rgba(173, 216, 230, 0.05)', name='BB Range'), row=1, col=1)
    fig.add_trace(go.Scatter(x=df['Time_Str'], y=df['MA9'], line=dict(color='#00f2ff', width=1.5), name='Trend'), row=1, col=1)

    # PANEL 2: RSI
    fig.add_trace(go.Scatter(x=df['Time_Str'], y=df['RSI'], line=dict(color='#ffaa00', width=2), name='RSI'), row=2, col=1)
    fig.add_hline(y=70, line_dash="dash", line_color="#ef4f60", row=2, col=1) 
    fig.add_hline(y=30, line_dash="dash", line_color="#3dc985", row=2, col=1)

    # PANEL 3: Color-Coded Volume
    fig.add_trace(go.Bar(x=df['Time_Str'], y=df['Volume'], marker_color=df['Vol_Color'], name='Volume'), row=3, col=1)

    # STYLING
    fig.update_layout(template='plotly_dark', xaxis_rangeslider_visible=False, height=900,
                      paper_bgcolor='#0b0d0f', plot_bgcolor='#0b0d0f',
                      margin=dict(l=10, r=80, t=50, b=10), hovermode='x unified')
    
    fig.update_xaxes(type='category', nticks=8)
    fig.update_yaxes(side='right', gridcolor='#1f2226')

    # LIVE PRICE ANNOTATION
    curr_p = float(df['Close'].iloc[-1])
    fig.add_annotation(xref="paper", yref="y1", x=1.02, y=curr_p, text=f"{cur}{curr_p:.2f}", 
                       showarrow=False, bgcolor="#00f2ff", font=dict(color="black", size=12, family="Arial Black"))

    fig.show()

if __name__ == "__main__":
    run_ultimate_broker_suite()
