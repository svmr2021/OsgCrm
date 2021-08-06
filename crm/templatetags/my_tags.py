import datetime
from django import template
from crm.models import *

register = template.Library()


@register.simple_tag
def get_balance():
    try:
        today = datetime.today().strftime('%Y-%m-%d')
        exchange = ExchangeRate.objects.get(date=today)

        object = Debt.objects.get_or_create()
        object = object[0]
        balances = Balance.objects.all()
        uzs = 0
        usd = 0
        for i in balances:
            if i.balance_type == 'UZS':
                uzs += i.amount
            elif i.balance_type == 'USD':
                usd += i.amount

        if object.amount_usz != uzs:
            object.amount_usz = 0
            object.save()
        if object.amount_usd != usd:
            object.amount_usd = 0
            object.save()

        balances = Balance.objects.all()
        for i in balances:
            if i.balance_type == 'UZS' and object.amount_usz != uzs:
                object.amount_usz += i.amount
            elif i.balance_type == 'USD' and object.amount_usd != usd:
                object.amount_usd += i.amount
        object.save()
        amount_uzs = object.amount_usd * exchange.one_dollar
        amount_usd = object.amount_usz / exchange.one_dollar
        amount_uzs = round(amount_uzs,3)
        amount_usd = round(amount_usd, 3)
        object.total_in_uzs = object.amount_usz + amount_uzs
        object.total_in_usd = amount_usd + object.amount_usd
        object.save()
        debt = object
        return debt
    except Exception as e:
        print(e)

