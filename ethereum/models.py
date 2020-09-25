from datetime import datetime
from .app import db



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
