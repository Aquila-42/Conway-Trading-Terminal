# 💎 The Conway Series: Ultimate Broker Suite

Welcome to the latest installment of the **"Conway Series"**—a personal collection of computational "side-quests" where I deconstruct complex systems for fun. This project is a high-performance, 3-panel interactive trading suite designed to visualize market microstructure in real-time.

## 🚀 Live Interactive Dashboard
**[PASTE YOUR GITHUB PAGES LINK HERE]**

---

## 💡 The "Conway" Story
Why the name? It started as a fun code-name for my early scripts, and now it serves as an "Easter Egg" throughout my portfolio. It represents the transition from theoretical physics to a quant-engineer who builds high-end tools just for the thrill of the build.

## 🛠️ Technical Highlights

### 1. Multi-Panel Microstructure Analysis
The dashboard is split into three synchronized zones to provide a complete view of an asset's health:
* **Zone 1 (Price & Volatility):** 1-minute Candlestick charts with **Bollinger Bands** (2σ) and a 9-period Trendline.
* **Zone 2 (Momentum):** A professional **Relative Strength Index (RSI)** implementing Wilder’s Smoothing logic.
* **Zone 3 (Volume):** Color-coded volume bars to verify price action strength.



### 2. Solving the "Categorical Time" Problem
Financial markets have gaps (nights/weekends). Standard plotting often shows these as empty spaces. I solved this by forcing the X-axis to render as **Categorical Strings**, ensuring a professional, continuous "Bloomberg-style" flow.

### 3. Quantitative Signal Logic
By layering Bollinger Bands over the price, the suite allows for "Volatility Breakout" detection. When the price touches the outer bands while RSI is in extreme territory, it flags potential mean-reversion opportunities.



---

## 🧰 Tech Stack
* **Graphics Engine:** Plotly (Interactive WebGL)
* **Data Feed:** yfinance (Real-time REST API)
* **Math:** NumPy, Pandas (Exponential Moving Averages & Volatility Calculation)

## 🧪 The "Fun" Part
The best part of this build was the **Live Price Tag**. Using a paper-reference coordinate system, the current price "floats" on the right-hand axis in a cyan-colored tag, giving it that modern, digital-terminal feel.

---
*Developed for the fun of deconstructing the market.*
