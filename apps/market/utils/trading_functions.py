from datetime import timedelta, timezone, datetime
import ccxt
from django.shortcuts import get_object_or_404
from apps.exchanges.models import Exchange
from apps.exchanges.utils.hyperliquid.download_data import download_data
from apps.market.backtesting.backtest_utils import run_backtest
from apps.market.models import PaperTrade, MarketData

def paper_trade_execute(trade_id):
    try:
        trade = PaperTrade.objects.get(id=trade_id)
        print(f"Trade: {trade}, Type: {type(trade)}")
    except PaperTrade.DoesNotExist:
        print("Trade not found.")
        return  # Optionally log this error

    if not trade.is_active:
        print("Trade is not active.")
        return  # Trade is not active, do nothing



    # Fetch exchange details from Exchange model using id_char
    exchange = get_object_or_404(Exchange, id_char=trade.exchange)
    print(f"Exchange: {exchange}, Type: {type(exchange)}")
    key = exchange.api_key
    secret = exchange.secret_key

    # Initialize the exchange instance, assuming CCXT usage
    exchange_class = getattr(ccxt, exchange.id_char)  # Ensure the name matches the CCXT identifier
    exchange_instance = exchange_class({
        'apiKey': key,
        'secret': secret,
        'timeout': 30000,
        'enableRateLimit': True,
    })
    print(f"Exchange Instance: {trade.exchange}, Type: {type(trade.exchange)}")

    # Define the timeframe for data to be fetched
    end_date = datetime.now()
    start_date = end_date - timedelta(days=trade.lookback_period)
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    print(f"Coin: {trade.coin}, Type: {type(trade.coin)}")
    print(f"Timeframe: {trade.timeframe}, Type: {type(trade.timeframe)}")
    print(f"Start Date: {start_date_str}, Type: {type(start_date_str)}")
    print(f"End Date: {end_date_str}, Type: {type(end_date_str)}")
    print(f"Exchange: {exchange_instance}, Type: {type(exchange_instance)}")

    # Download data using the utility function
    df = download_data(trade.coin, trade.timeframe, start_date_str, end_date_str, exchange_instance)
    print(f"Downloaded data: {df}, Type: {type(df)}")

    # TODO: To implement comission and openbrowser
    # Run backtest using the utility function
    st, price = run_backtest(trade.coin, df, trade.timeframe, trade.initial_balance, commission=0.008, openbrowser=False, atr_timeperiod=trade.atr_timeperiod, atr_multiplier=trade.atr_multiplier)
    print(f"Backtest results: st: {st}, Type: {type(st)}, price: {price}, Type: {type(price)}")

    # Calculate Volume and Volatility
    volume_change, volatility = calculate_volume_and_volatility(df)

    # Save to MarketData
    MarketData.objects.create(
        paper_trade=trade,
        timestamp=end_date,
        price=price,
        st=st,
        super_trend_status='long' if st > price else 'short',
        volume=volume_change['current'],
        vol_5m=volatility['5m'],
        vol_15m=volatility['15m'],
        vol_30m=volatility['30m'],
        vol_1h=volatility['1h'],
        vol_change_5m=volume_change['5m'],
        vol_change_15m=volume_change['15m'],
        vol_change_30m=volume_change['30m'],
        vol_change_1h=volume_change['1h']
    )
    print("Market data saved.")

def calculate_volume_and_volatility(df):
    # Assuming df has 'Volume' and price columns for calculating changes and volatility
    volume_change = {}
    volatility = {}

    for period in ['5m', '15m', '30m', '1h']:
        resampled = df.resample(period).last()
        volume_change[period] = resampled['Volume'].pct_change()[-1]
        volatility[period] = resampled['Close'].pct_change().rolling(window=int(period[:-1])).std()[-1]

    return volume_change, volatility