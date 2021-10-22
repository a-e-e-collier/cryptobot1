from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect
from utils import main
from utils import db

from managetemplate.models import Settings
import json

def settings(request):
    data_json = request.body
    data = json.loads(data_json)
    address = data["address"]
    private_key = data["private_key"]
    network = data["network"]
    provider = data["provider"]
    gas_limit = int(data["gas_limit"])
    slippage = float(data["slippage"])
    gas_price = float(data["gas_price"]) * 10 ** 9
    eth_amount = float(data["eth_amount"]) * 10 ** 18
    smart_contract = data["smart_contract"]
    Settings.objects.all().delete()
    template = Settings(address=address,
                        private_key=private_key,
                        network=network,
                        provider=provider,
                        gas_limit=gas_limit,
                        slippage=slippage,
                        gas_price=gas_price,
                        eth_amount=eth_amount,
                        smart_contract=smart_contract)
    template.save()
    data = {
        'success': True
    }
    return JsonResponse(data)

def index(request):
    address, private_key, network, provider, gas_limit, slippage, gas_price, eth_amount, smart_contract = db.get_params('all')
    gas_price = gas_price / (10 ** 9)
    if gas_price.is_integer():
        gas_price = int(gas_price)
    eth_amount = eth_amount / (10 ** 18)
    if eth_amount.is_integer():
        eth_amount = int(eth_amount)
    if slippage.is_integer():
        slippage = int(slippage)

    context = {
        "address": address,
        "private_key": private_key,
        "network": network,
        "provider": provider,
        "gas_limit": gas_limit,
        "slippage": slippage,
        "gas_price": gas_price,
        "eth_amount": eth_amount,
        "smart_contract": smart_contract
    }

    return render(request, 'index.html', context=context)

def startbot(request):
    hex = main.main()


    data = {
        'success': True,
        'hex': hex
    }
    return JsonResponse(data)