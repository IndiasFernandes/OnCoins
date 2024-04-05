# exchanges/models.py
from django.db import models

class Exchange(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    api_url = models.URLField()
    def __str__(self):
        return self.name

class Market(models.Model):
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)  # Example: BTC/USD
    def __str__(self):
        return self.symbol

class HistoricalData(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    open_price = models.DecimalField(max_digits=15, decimal_places=5)
    close_price = models.DecimalField(max_digits=15, decimal_places=5)
    high_price = models.DecimalField(max_digits=15, decimal_places=5)
    low_price = models.DecimalField(max_digits=15, decimal_places=5)
    volume = models.DecimalField(max_digits=15, decimal_places=5)
    timestamp = models.DateTimeField()
    def __str__(self):
        return f'{self.market.symbol} {self.timestamp}'

class ExchangeInfo(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    account_value = models.DecimalField(max_digits=10, decimal_places=2)
    total_margin_used = models.DecimalField(max_digits=10, decimal_places=2)
    total_net_position = models.DecimalField(max_digits=10, decimal_places=2)
    total_raw_usd = models.DecimalField(max_digits=10, decimal_places=2)
    withdrawable = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Exchange Information"
