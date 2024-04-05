from django.shortcuts import render
from bots.models import Bot, Trade

def dashboard(request):
    bots = Bot.objects.all()
    active_bots_count = bots.filter(is_active=True).count()
    # Pass it to your context
    trades = Trade.objects.all().order_by('-timestamp')[:5]
    context = {'bots': bots, 'active_bots_count': active_bots_count, 'trades': trades}

    return render(request, 'pages/general/dashboard.html', context)