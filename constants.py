TARGET_TICKERS: list[str] = [
	"AAPL",
	"MSFT",
	"AMZN",
    "NVDA",
    "TSLA",
    "META",
    "ORCL",
    "UNH",
    "V",
    "JPM",
    "BAC",
    "MA",
    "WMT",
    "PG",
    "DIS",
    "NFLX",
    "INTC",
    "AMD",
    "PLUG",
    "SOFI",
    "RIVN",
    "COIN",
    "BA",
    "MCD",
]
# Examples: ["AAPL", "MSFT", "NVDA"]
TIME_FRAME: str = "1y"
# Examples: "1d", "5d", "1mo", "6mo", "1y", "5y", "max"
INTERVAL: str = "1m"
# Examples: "1m", "5m", "15m", "1h", "1d", "1wk"
CALL_DELAY_SECONDS: float = 10.0
# Examples: 0.5, 1.0, 2.0
CALL_LIMIT: int = 20
# Examples: 5, 20, 100
OUTPUT_DIR: str = "/Users/kristopherpepper/Documents/jupyterProjects/historicalStockDataDownload2/output"
# Absolute directory where CSV exports are saved.
