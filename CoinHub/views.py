from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from apps.bots.models import Bot, Trade
from apps.exchanges.models import ExchangeInfo
from apps.market.models import PaperTrade

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/general/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bots = Bot.objects.all()
        context['bots'] = bots
        context['active_bots_count'] = bots.filter(is_active=True).count()
        context['trades'] = Trade.objects.all().order_by('-timestamp')[:5]
        context['show_sidebar'] = False

        # Account value chart data
        exchange_infos = ExchangeInfo.objects.all().order_by('timestamp')
        context['timestamps'] = [info.timestamp.strftime("%Y-%m-%d %H:%M:%S") for info in exchange_infos]
        context['account_values'] = [float(info.account_value) for info in exchange_infos]
        context['withdrawable_values'] = [float(info.withdrawable) for info in exchange_infos]

        # Paper trades
        context['paper_trades'] = PaperTrade.objects.all()

        return context

class AboutView(TemplateView):
    template_name = 'about.html'


import subprocess
from django.http import HttpResponse

def activate_ssh(request):
    try:
        # Execute the command to activate SSH
        subprocess.run(["sudo", "systemctl", "enable", "ssh"], check=True)
        subprocess.run(["sudo", "systemctl", "start", "ssh"], check=True)
        # Return a success response
        return HttpResponse("SSH activated successfully.")
    except subprocess.CalledProcessError as e:
        # Return an error response if the command fails
        error_message = f"Error activating SSH: {e}"
        return HttpResponse(error_message, status=500)