import os

from flask_api import FlaskAPI, status
from flask_sqlalchemy import SQLAlchemy
from .models import Ether, Gas


app = FlaskAPI(__name__)

db_uri = f'{os.path.abspath(os.getcwd())}/db/db.sqlite3'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_uri}'

db = SQLAlchemy(app)


@app.route('/ether/', methods=['GET'])
def get_ether():
    data = {}

    try:
        ether = Ether.query.filter_by().all()[-1]
        data['created'] = ether.created
        data['price'] = ether.price_usd
        return data

    except:
        return {"error": "not found"}, status.HTTP_404_NOT_FOUND


@app.route('/gas/', methods=['GET'])
def get_gas():
    data = {}

    try:
        gas = Gas.query.filter_by().all()[-1]
        data['created'] = gas.created
        data['safe_gas_price'] = gas.safe_gas_price
        data['propose_gas_price'] = gas.propose_gas_price
        data['fast_gas_price'] = gas.fast_gas_price
        return data

    except:
        return {"error": "not found"}, status.HTTP_404_NOT_FOUND


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
