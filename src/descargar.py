import yfinance as yf

df = yf.download("NVDA", start="2021-01-01", auto_adjust=True)
df.columns = df.columns.get_level_values(0)
df.to_csv("data/raw/nvda.csv")
print(df.tail())
print(f"\nFilas descargadas: {len(df)}")
