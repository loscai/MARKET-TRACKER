import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

import yfinance as yf


'''
ESEMPI CHE MI SALVO:
GOOG - Google
AAPL - Apple
MSFT - Microsoft
AMZN - Amazon
NVDA - NVIDIA
'''

nAnni = 5
periodo = str(nAnni) + "y"
ticker = "GOOG"
data = yf.download(ticker, period=periodo)

# Creazione dei vettori associativi con valori corretti
close_prices = {date.strftime("%Y-%m-%d"): str(row["Close"].item()) for date, row in data.iterrows()}
high_prices = {date.strftime("%Y-%m-%d"): str(row["High"].item()) for date, row in data.iterrows()}
low_prices = {date.strftime("%Y-%m-%d"): str(row["Low"].item()) for date, row in data.iterrows()}
open_prices = {date.strftime("%Y-%m-%d"): str(row["Open"].item()) for date, row in data.iterrows()}
volume_data = {date.strftime("%Y-%m-%d"): str(row["Volume"].item()) for date, row in data.iterrows()}

# Converti i dati del dizionario in un formato utilizzabile per il grafico
dates = [datetime.strptime(date, "%Y-%m-%d") for date in close_prices.keys()]
close_values = [float(price) for price in close_prices.values()]
high_values = [float(price) for price in high_prices.values()]
low_values = [float(price) for price in low_prices.values()]
volume_values = [float(vol) for vol in volume_data.values()]

# Ottieni il nome completo dell'azienda
ticker_info = yf.Ticker(ticker)
company_name = ticker_info.info.get('longName', ticker)  # usa il ticker come fallback se longName non è disponibile

# Crea una figura con due sottografici (prezzo e volume)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 10), gridspec_kw={'height_ratios': [3, 1]})
fig.suptitle(f'{company_name} ({ticker}) Prezzo delle Azioni - {nAnni} {"Anno" if nAnni == 1 else "Anni"}', fontsize=16)
plt.get_current_fig_manager().set_window_title(f'{company_name} - Market Tracker')

# Traccia il prezzo di chiusura
ax1.plot(dates, close_values, 'b-', label='Prezzo di Chiusura')
ax1.set_ylabel('Prezzo (USD)')
ax1.set_title('Storico dei Prezzi')
ax1.grid(True, alpha=0.3)
ax1.legend()

# Aggiungi indicatori di prezzo massimo e minimo
ax1.fill_between(dates, low_values, high_values, alpha=0.2, color='blue', label='Intervallo Max-Min')

# Traccia il volume
ax2.bar(dates, volume_values, color='green', alpha=0.5, label='Volume')
ax2.set_ylabel('Volume')
ax2.set_xlabel('Data')
ax2.grid(True, alpha=0.3)
ax2.set_axisbelow(True)
ax2.legend()

# Formatta l'asse delle date
for ax in [ax1, ax2]:
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)

# Aggiungi una media mobile al grafico dei prezzi (50 giorni)
window_size = 50
if len(close_values) >= window_size:
    moving_avg = np.convolve(close_values, np.ones(window_size)/window_size, mode='valid')
    ma_dates = dates[window_size-1:]
    ax1.plot(ma_dates, moving_avg, 'r-', label=f'Media Mobile a {window_size} giorni')
    ax1.legend()

# Sistema il layout
plt.tight_layout()
plt.subplots_adjust(top=0.9)

# Mostra il grafico
plt.show()

# Opzionale: Salva la figura
# plt.savefig('google_stock_chart.png', dpi=300, bbox_inches='tight')