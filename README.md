# 📈 Market Tracker 🇺🇸

A Python application that creates interactive stock market charts using data from Yahoo Finance.

## 📝 Description

This application allows you to visualize stock market data with the following features:

- 📊 Stock price history
- 📉 Volume data
- 📈 50-day moving average
- 🔍 Price range (High-Low) visualization

## ⚙️ Requirements

```bash
pip install matplotlib
pip install yfinance
pip install numpy
```

## 🚀 Usage

### 🔧 Configuration

```python
nAnni = 5  # Number of years to analyze
ticker = "GOOG"  # Stock symbol
```

### 💹 Available Tickers

#### 🖥️ Tech Companies
- AAPL - Apple Inc.
- GOOG - Google
- MSFT - Microsoft
- AMZN - Amazon
- NVDA - NVIDIA
- INTC - Intel Corporation
- PLTR - Palantir Technologies Inc.
- SMCI - Super Micro Computer, Inc.
- SOUN - SoundHound AI, Inc.

#### 🚗 Automotive & Transportation
- TSLA - Tesla, Inc.
- F - Ford Motor Company
- LCID - Lucid Group, Inc.
- AAL - American Airlines Group Inc.
- NIO - NIO Inc.

#### 🏦 Financial Services
- HOOD - Robinhood Markets, Inc.
- NU - Nu Holdings Ltd.
- BBD - Banco Bradesco S.A.

#### ⚡ Quantum Computing
- QBTS - D-Wave Quantum Inc.
- RGTI - Rigetti Computing, Inc.
- IONQ - IonQ, Inc.

#### 🌍 Mining & Resources
- BTG - B2Gold Corp.
- VALE - Vale S.A.
- PSLV - Sprott Physical Silver Trust
- RIG - Transocean Ltd.

#### 🍺 Consumer Goods
- ABEV - Ambev S.A.

#### 🔐 Cryptocurrency Related
- MARA - MARA Holdings, Inc.

### ▶️ Running the Application

```bash
python main.py
```

## 🎯 Features

### 📊 Main Chart
- 🔵 Blue line: Closing prices
- 📊 Blue shaded area: Price range (High-Low)
- 🔴 Red line: 50-day moving average

### 📈 Volume Chart
- 🟢 Green bars: Trading volume

## 🖥️ Output

The application generates an interactive window showing:

1. 📈 Stock price history
2. 📊 Trading volume
3. 📉 Moving averages
4. 🔍 Price ranges

## ⚡ Optional Features

You can save the chart as an image by uncommenting the following line:

```python
# plt.savefig('google_stock_chart.png', dpi=300, bbox_inches='tight')
```

## 🛠️ Technical Details

- 🌐 Data Source: Yahoo Finance API
- 📊 Charting Library: Matplotlib
- 🔢 Data Processing: NumPy

---

# 📈 Tracciatore di Mercato 🇮🇹

Un'applicazione Python che crea grafici interattivi del mercato azionario utilizzando i dati di Yahoo Finance.

## 📝 Descrizione

Questa applicazione permette di visualizzare i dati del mercato azionario con le seguenti caratteristiche:

- 📊 Storico dei prezzi delle azioni
- 📉 Dati sul volume
- 📈 Media mobile a 50 giorni
- 🔍 Visualizzazione dell'intervallo dei prezzi (Massimo-Minimo)

## ⚙️ Requisiti

```bash
pip install matplotlib
pip install yfinance
pip install numpy
```

## 🚀 Utilizzo

### 🔧 Configurazione

```python
nAnni = 5  # Numero di anni da analizzare
ticker = "GOOG"  # Simbolo dell'azione
```
### 💹 Ticker Disponibili

#### 🖥️ Aziende Tecnologiche
- AAPL - Apple Inc.
- GOOG - Google
- MSFT - Microsoft
- AMZN - Amazon
- NVDA - NVIDIA
- INTC - Intel Corporation
- PLTR - Palantir Technologies Inc.
- SMCI - Super Micro Computer, Inc.
- SOUN - SoundHound AI, Inc.

#### 🚗 Automotive e Trasporti
- TSLA - Tesla, Inc.
- F - Ford Motor Company
- LCID - Lucid Group, Inc.
- AAL - American Airlines Group Inc.
- NIO - NIO Inc.

#### 🏦 Servizi Finanziari
- HOOD - Robinhood Markets, Inc.
- NU - Nu Holdings Ltd.
- BBD - Banco Bradesco S.A.

#### ⚡ Computazione Quantistica
- QBTS - D-Wave Quantum Inc.
- RGTI - Rigetti Computing, Inc.
- IONQ - IonQ, Inc.

#### 🌍 Mineraria e Risorse
- BTG - B2Gold Corp.
- VALE - Vale S.A.
- PSLV - Sprott Physical Silver Trust
- RIG - Transocean Ltd.

#### 🍺 Beni di Consumo
- ABEV - Ambev S.A.

#### 🔐 Correlati alle Criptovalute
- MARA - MARA Holdings, Inc.

### ▶️ Esecuzione dell'Applicazione

```bash
python main.py
```

## 🎯 Funzionalità

### 📊 Grafico Principale
- 🔵 Linea blu: Prezzi di chiusura
- 📊 Area blu ombreggiata: Intervallo dei prezzi (Massimo-Minimo)
- 🔴 Linea rossa: Media mobile a 50 giorni

### 📈 Grafico del Volume
- 🟢 Barre verdi: Volume degli scambi

## 🖥️ Output

L'applicazione genera una finestra interattiva che mostra:

1. 📈 Storico dei prezzi delle azioni
2. 📊 Volume degli scambi
3. 📉 Medie mobili
4. 🔍 Intervalli di prezzo

## ⚡ Funzionalità Opzionali

Puoi salvare il grafico come immagine decommentando la seguente riga:

```python
# plt.savefig('google_stock_chart.png', dpi=300, bbox_inches='tight')
```

## 🛠️ Dettagli Tecnici

- 🌐 Fonte dei dati: Yahoo Finance API
- 📊 Libreria per i grafici: Matplotlib
- 🔢 Elaborazione dati: NumPy

## 👨‍💻 Author / Autore

[ Colombo Christian ]