# exchanges/exchange_data.py

EXCHANGES = {
    'hyperliquid': {
        'name': 'HyperLiquid',
        'symbols': [
            'AAVE/USDC:USDC', 'ACE/USDC:USDC', 'ADA/USDC:USDC', 'AI/USDC:USDC',
            'ALT/USDC:USDC', 'APE/USDC:USDC', 'APT/USDC:USDC', 'AR/USDC:USDC',
            'ARB/USDC:USDC', 'ARK/USDC:USDC', 'ATOM/USDC:USDC', 'AVAX/USDC:USDC',
            'BADGER/USDC:USDC', 'BANANA/USDC:USDC', 'BCH/USDC:USDC', 'BIGTIME/USDC:USDC',
            'BLUR/USDC:USDC', 'BLZ/USDC:USDC', 'BNB/USDC:USDC', 'BNT/USDC:USDC',
            'BOME/USDC:USDC', 'BSV/USDC:USDC', 'BTC/USDC:USDC', 'CAKE/USDC:USDC',
            'CANTO/USDC:USDC', 'CFX/USDC:USDC', 'COMP/USDC:USDC', 'CRV/USDC:USDC',
            'CYBER/USDC:USDC', 'DOGE/USDC:USDC', 'DOT/USDC:USDC', 'DYDX/USDC:USDC',
            'DYM/USDC:USDC', 'ENA/USDC:USDC', 'ENS/USDC:USDC', 'ETC/USDC:USDC',
            'ETH/USDC:USDC', 'ETHFI/USDC:USDC', 'FET/USDC:USDC', 'FIL/USDC:USDC',
            'FRIEND/USDC:USDC', 'FTM/USDC:USDC', 'FTT/USDC:USDC', 'FXS/USDC:USDC',
            'GALA/USDC:USDC', 'GAS/USDC:USDC', 'GMT/USDC:USDC', 'GMX/USDC:USDC',
            'HPOS/USDC:USDC', 'ILV/USDC:USDC', 'IMX/USDC:USDC', 'INJ/USDC:USDC',
            'JTO/USDC:USD', 'JUP/USDC:USDC', 'KAS/USD:USDC', 'LDO/USDC:USDC',
            'LINK/USDC:USDC', 'LOOM/USDC:USDC', 'LTC/USDC:USDC', 'MANTA/USDC:USDC',
            'MATIC/USDC:USDC', 'MAV/USDC:USDC', 'MAVIA/USDC:USDC', 'MEME/USDC:USDC',
            'MINA/USDC:USDC', 'MKR/USDC:USDC', 'MNT/USDC:USDC', 'MYRO/USDC:USDC',
            'NEAR/USDC:USDC', 'NEO/USDC:USDC', 'NFTI/USDC:USDC', 'NTRN/USDC:USDC',
            'OGN/USDC:USDC', 'ONDO/USDC:USDC', 'OP/USDC:USDC', 'ORBS/USDC:USDC',
            'ORDI/USDC:USDC', 'OX/USDC:USDC', 'PANDORA/USDC:USDC', 'PENDLE/USDC:USDC',
            'PEOPLE/USDC:USDC', 'PIXEL/USDC:USDC', 'POLYX/USDC:USDC', 'PYTH/USDC:USDC',
            'RDNT/USDC:USDC', 'REQ/USDC:USDC', 'RLB/USDC:USDC', 'RNDR/USDC:USDC',
            'RSR/USDC:USDC', 'RUNE/USDC:USDC', 'SEI/USDC:USDC', 'SHIA/USDC:USDC',
            'SNX/USDC:USDC', 'SOL/USDC:USDC', 'STG/USDC:USDC', 'STRAX/USDC:USDC',
            'STRK/USDC:USDC', 'STX/USDC:USDC', 'SUI/USDC:USDC', 'SUPER/USDC:USDC',
            'SUSHI/USDC:USDC', 'TAO/USDC:USDC', 'TIA/USDC:USDC', 'TNSR/USDC:USDC',
            'TON/USDC:USDC', 'TRB/USDC:USDC', 'TRX/USDC:USDC', 'UMA/USDC:USDC',
            'UNI/USDC:USDC', 'UNIBOT/USDC:USDC', 'USTC/USDC:USDC', 'W/USDC:USDC',
            'WIF/USDC:', 'WLD/USDC:USDC', 'XAI/USDC:USDC', 'XRP/USDC:USDC',
            'YGG/USDC:', 'ZEN/USDC:USDC', 'ZETA/USDC:USDC', 'ZRO/USDC:USDC',
            'kBONK/USDC:USDC', 'kFLOKI/USDC:USDC', 'kLUNC/USDC:USDC', 'kPEPE/USDC:USDC',
            'kSHIB/USDC:USDC'
        ],
        'timeframes': [
            '1m', '5m', '15m', '30m', '1h', '4h', '1d', '1w', '1M'
        ]
    },
    'binance': {
        'name': 'Binance',
        'symbols': [
            'BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'ADA/USDT',
            'XRP/USDT', 'SOL/USDT', 'DOT/USDT', 'DOGE/USDT',
            'AVAX/USDT', 'SHIB/USDT', 'MATIC/USDT', 'LTC/USDT',
            'UNI/USDT', 'LINK/USDT', 'BCH/USDT', 'XLM/USDT',
            'ATOM/USDT', 'FTT/USDT', 'ALGO/USDT', 'VET/USDT'
        ],
        'timeframes': [
            '1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M'
        ]
    },
    'coinbase': {
        'name': 'Coinbase',
        'symbols': [
            'BTC/USD', 'ETH/USD', 'LTC/USD', 'BCH/USD',
            'ETC/USD', 'ZRX/USD', 'BAT/USD', 'ZEC/USD',
            'MANA/USD', 'LOOM/USD', 'DNT/USD', 'CVC/USD',
            'REP/USD', 'KNC/USD', 'OMG/USD', 'GNT/USD',
            'DAI/USD', 'USDC/USD', 'MKR/USD', 'PAX/USD'
        ],
        'timeframes': [
            '1m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '1d', '1w', '1M'
        ]
    },
    'kraken': {
        'name': 'Kraken',
        'symbols': [
            'BTC/EUR', 'ETH/EUR', 'XRP/EUR', 'LTC/EUR',
            'BCH/EUR', 'EOS/EUR', 'ADA/EUR', 'XLM/EUR',
            'LINK/EUR', 'TRX/EUR', 'DOT/EUR', 'UNI/EUR',
            'XMR/EUR', 'ATOM/EUR', 'XTZ/EUR', 'FIL/EUR',
            'YFI/EUR', 'COMP/EUR', 'AAVE/EUR', 'MKR/EUR'
        ],
        'timeframes': [
            '1m', '5m', '15m', '30m', '1h', '4h', '1d', '1w'
        ]
    }
}
