# forms.py
from datetime import datetime, timedelta
from .exchange_data import EXCHANGES
from .models import Exchange
from django import forms
from .models import Market



class DownloadDataForm(forms.Form):
    exchange_id = forms.ChoiceField(choices=[(key, value['name']) for key, value in EXCHANGES.items()], label="Exchange")
    symbol = forms.MultipleChoiceField(choices=[], label="Symbol")
    timeframe = forms.MultipleChoiceField(choices=[], label="Timeframe")
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),
                                 initial=datetime.now().replace(day=1).strftime('%Y-%m-%d'))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),
                               initial=(datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'exchange_id' in self.data:
            exchange_id = self.data.get('exchange_id')
            exchange_data = EXCHANGES.get(exchange_id)
            if exchange_data:
                self.fields['symbol'].choices = [(symbol, symbol) for symbol in exchange_data['symbols']]
                self.fields['timeframe'].choices = [(timeframe, timeframe) for timeframe in exchange_data['timeframes']]
        else:
            # Set default choices
            default_exchange = list(EXCHANGES.keys())[0]
            self.fields['symbol'].choices = [(symbol, symbol) for symbol in EXCHANGES[default_exchange]['symbols']]
            self.fields['timeframe'].choices = [(timeframe, timeframe) for timeframe in EXCHANGES[default_exchange]['timeframes']]

class ExchangeForm(forms.ModelForm):
    class Meta:
        model = Exchange
        fields = ['name', 'description', 'api_url', 'api_key', 'secret_key', 'id_char']


# In forms.py
from django import forms
from .models import Market, Exchange

class MarketForm(forms.ModelForm):
    exchange = forms.ModelChoiceField(queryset=Exchange.objects.all(), to_field_name='id_char', required=True)

    class Meta:
        model = Market
        fields = ['market_type', 'coins', 'exchange']
        widgets = {
            'coins': forms.CheckboxSelectMultiple,
        }
