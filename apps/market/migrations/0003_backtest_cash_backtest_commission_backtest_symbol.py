# Generated by Django 5.0.4 on 2024-04-12 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_backtest_delete_backtests'),
    ]

    operations = [
        migrations.AddField(
            model_name='backtest',
            name='cash',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='backtest',
            name='commission',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='backtest',
            name='symbol',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]