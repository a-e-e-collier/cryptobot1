from utils import uniswap
from utils import db
# import config as cf
import time
import requests
import json
import datetime
import os
import sys

def add_token(_token, _address, network='mainnet'):
    path = os.path.join(os.path.abspath(os.getcwd()), "assets")
    full_path = os.path.join(path, "contract_addresses.JSON")
    with open(full_path) as f:
        full_data_file = json.load(f)
        token_and_exchange_addresses = full_data_file[network]
    if _token not in token_and_exchange_addresses.keys():
        full_data_file[network][_token] = _address

        with open(full_path, 'w') as fp:
            json.dump(full_data_file, fp, indent=4)

def do():

    val = datetime.datetime.now()
    uniswap_wrapper1 = uniswap.Uniswap(address=ADDRESS,
                                                 private_key=PRIVATE_KEY,
                                                 provider=PROVIDER,
                                                 version=1,
                                                 max_slippage=SLIPPAGE)
    uniswap_wrapper2 = uniswap.Uniswap(address=ADDRESS,
                                                 private_key=PRIVATE_KEY,
                                                 provider=PROVIDER,
                                                 version=2,
                                                 max_slippage=SLIPPAGE)

    uni_contract = uniswap_wrapper1.exchange_address_from_token(SMART_CONTRACT)
    add_token(SMART_CONTRACT, uni_contract)

    try:
        token_balance = uniswap_wrapper2.get_eth_token_input_price(SMART_CONTRACT,1*10**18)
        convert_bal = token_balance / 1000000000000000000 #this token has 18 decimal and wrtitten in 18 zeros, if it is 9 decimal please replace this to 9 zeros
        print(convert_bal)

        if convert_bal >= 0.001:
            t1 = uniswap_wrapper2._eth_to_token_swap_input(SMART_CONTRACT, ETH_AMOUNT, None)
            print(f"Transaction token to eth : https://etherscan.io/tx/{t1.hex()}")
            print("Done")
            return 0, f"https://etherscan.io/tx/{t1.hex()}"
        else:
            print("No liquidity detected")
            return 1, 1

    except:
        print("No liquidity detected")
        return 2, 2
def test():
    print(ETH_AMOUNT)

def main():
    global ADDRESS, PRIVATE_KEY, PROVIDER, SLIPPAGE, ETH_AMOUNT, SMART_CONTRACT
    ADDRESS, PRIVATE_KEY, PROVIDER, SLIPPAGE, ETH_AMOUNT, SMART_CONTRACT = db.get_params("main")

    uniswap.set_param()

    val = 10000
    while True:
        val, hex = do()
        if val == 0:
            print(hex)
            return hex
        time.sleep(1)