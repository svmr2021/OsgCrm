from django.test import TestCase

# Create your tests here.
from datetime import datetime
import requests
from django.utils import timezone

print(datetime.now().strftime('%H:%M'))
x = requests.get('https://nbu.uz/exchange-rates/json/').json()

for i in x:
    print(i)
    if i['code'] == 'USD':
        usd = i['nbu_cell_price']
