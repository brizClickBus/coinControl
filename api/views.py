from django.shortcuts import render
import requests
from django.utils import timezone
from bank.models import CentralBank

url = "https://brasilapi.com.br/api/banks/v1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("A requisição falhou")

bancos = CentralBank()
for banco in data:
    if banco['code'] == None:
        code = 0
    else:
        code = banco['code']
    CentralBank.objects.create(
        ispb=banco['ispb'],
        name = banco['name'],
        code = code,
        fullName = banco['fullName'],
        lastUpdate = timezone.now()
    )

    bancos.ispb = banco['ispb']
    bancos.name = banco['name']
    if banco['code'] == None:
        bancos.code = 0
    else:
        bancos.code = banco['code']

    bancos.fullName = banco['fullName']
    bancos.lastUpdate = timezone.now()
    bancos.save()

