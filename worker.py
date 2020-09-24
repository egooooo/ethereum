import time
import requests

import app


class DataWorker:

    def __init__(self):
        self.ether_api_token = 'RDGHT2SH2N6434F5M44BD3FZAR2S9ZEA1P'

    def run(self):
        self.get_gas()
        self.get_ether()

    def get_gas(self):
        response = requests.get(
            url=f'https://api.etherscan.io/api?module=gastracker&'
                f'action=gasoracle&apikey={self.ether_api_token}'
        )

        print(f'GAS: {response.json()}')
        gas = app.Gas(
            safe_gas_price=response.json()['result']['SafeGasPrice'],
            propose_gas_price=response.json()['result']['ProposeGasPrice'],
            fast_gas_price=response.json()['result']['FastGasPrice']
        )
        db = app.db
        db.session.add(gas)
        db.session.commit()

        return True

    def get_ether(self):
        response = requests.get(
            url=f'https://api.etherscan.io/api?module=stats&'
                f'action=ethprice&apikey={self.ether_api_token}'
        )
        ether = app.Ether(
            price_usd=response.json()['result']['ethusd']
        )
        db = app.db
        db.session.add(ether)
        db.session.commit()

        print(f'ETHER: {response.json()}')
        return True


if __name__ == "__main__":
    worker = DataWorker()

    while True:
        time.sleep(5)
        print(f"Tick")
        worker.run()
