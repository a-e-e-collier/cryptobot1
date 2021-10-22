from managetemplate.models import Settings

def get_params(param):

    data = Settings.objects.raw(""
                                      "SELECT "
                                      "    * "
                                      "FROM "
                                      "    managetemplate_settings "
                                      )

    data_list = list(data)
    for item in data_list:
        address = item.address
        private_key = item.private_key
        network = item.network
        provider = item.provider
        gas_limit = item.gas_limit
        slippage = item.slippage
        gas_price = item.gas_price
        eth_amount = item.eth_amount
        smart_contract = item.smart_contract
        if param == 'main':
            return address, private_key, provider, slippage, eth_amount, smart_contract
        if param == 'api':
            return gas_limit, gas_price, network
        if param == 'all':
            return address, private_key, network, provider, gas_limit, slippage, gas_price, eth_amount, smart_contract


