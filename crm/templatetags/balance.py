import datetime
from django import template
from crm.models import *
register = template.Library()


@register.simple_tag
def get_balance(user):
    try:
        object = Debt.objects.get_or_create(user=user)
        object = object[0]
        balances = Balance.objects.all()
        uzs = 0
        usd = 0
        for i in balances:
            if i.balance_type == 'UZS':
                uzs += i.amount
            elif i.balance_type == 'USD':
                usd +=i.amount

        if object.amount_usz != uzs:
            object.amount_usz = 0
            object.save()
        if object.amount_usd != usd:
            object.amount_usd = 0
            object.save()

        for i in balances:
            if i.balance_type == 'UZS' and object.amount_usz != uzs:
                object.amount_usz += i.amount
                object.save()
            elif i.balance_type == 'USD' and object.amount_usd != usd:
                object.amount_usd += i.amount
                object.save()
        debt_amount = object
        return debt_amount
    except Exception as e:
        print(e)