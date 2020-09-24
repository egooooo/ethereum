import os

from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = FlaskAPI(__name__)

db_uri = f'{os.path.abspath(os.getcwd())}/db/db.sqlite3'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_uri}'

db = SQLAlchemy(app)


class AbstractBaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.now)
    updated = db.Column(db.DateTime, default=datetime.now)


class Ether(AbstractBaseModel):
    price_usd = db.Column(db.String(31))


class Gas(AbstractBaseModel):
    safe_gas_price = db.Column(db.String(13))
    propose_gas_price = db.Column(db.String(13))
    fast_gas_price = db.Column(db.String(13))


@app.route('/ether/', methods=['GET'])
def get_ether():
    data = {}

    ether = Ether.query.filter_by().all()[-1]

    data['created'] = ether.created
    data['price'] = ether.price_usd

    return data


@app.route('/gas/', methods=['GET'])
def get_gas():
    data = {}

    gas = Gas.query.filter_by().all()[-1]

    data['created'] = gas.created
    data['safe_gas_price'] = gas.safe_gas_price
    data['propose_gas_price'] = gas.propose_gas_price
    data['fast_gas_price'] = gas.fast_gas_price

    return data


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
