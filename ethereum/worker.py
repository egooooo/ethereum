import time
import requests

from .app import app


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
        # TODO
        gas = app.Gas(
            safe_gas_price=response.json()['result']['SafeGasPrice'],
            propose_gas_price=response.json()['result']['ProposeGasPrice'],
            fast_gas_price=response.json()['result']['FastGasPrice']
        )
        db = app.db
        db.session.add(gas)
        db.session.commit()


    def get_ether(self):
        response = requests.get(
            url=f'https://api.etherscan.io/api?module=stats&'
                f'action=ethprice&apikey={self.ether_api_token}'
        )
        # TODO
        ether = app.Ether(
            price_usd=response.json()['result']['ethusd']
        )
        db = app.db
        db.session.add(ether)
        db.session.commit()


if __name__ == "__main__":
    worker = DataWorker()

    while True:
        time.sleep(5)
        print(f"Tick")
        # sys.stdout.write(f'Tick')
        worker.run()
