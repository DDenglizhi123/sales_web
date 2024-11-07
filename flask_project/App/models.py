from .extentions import db

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_name = db.Column(db.String(255), nullable=False)
    tin_number=db.Column(db.String(255), nullable=True)
    vrn_number=db.Column(db.String(255), nullable=True)
    address_1=db.Column(db.String(255), nullable=True)
    address_2=db.Column(db.String(255), nullable=True)
    address_3=db.Column(db.String(255), nullable=True)
    city=db.Column(db.String(255), nullable=True)
    country=db.Column(db.String(255), nullable=True)
    contact_name=db.Column(db.String(255), nullable=True)
    contact_number=db.Column(db.String(255), nullable=True)

class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class Lpos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lpo_number=db.Column(db.String(255), nullable=True)


class ProductInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    serial_number=db.Column(db.String(255), nullable=False)
    item_number=db.Column(db.String(255), nullable=False)
    key_word=db.Column(db.String(255), nullable=False)
    specification=db.Column(db.String(255), nullable=False)
    stock_qty = db.Column(db.Integer, nullable=False)
    unit_price_exclusive=db.Column(db.String(255), nullable=False)
    unit=db.Column(db.String(255), nullable=False)
    stock_redline=db.Column(db.String(255), nullable=False)
    purchase_qty_under_redline=db.Column(db.Integer, nullable=False)

