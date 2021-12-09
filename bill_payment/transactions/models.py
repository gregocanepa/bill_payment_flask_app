from bill_payment import db


class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    amount = db.Column(db.Float(), nullable=False)
    payment_method = db.Column(db.String(length=200), nullable=False)
    card_number = db.Column(db.String(length=200), nullable=True)
    bar_code = db.Column(db.String(length=1024), nullable=False, unique=True)
    payment_date = db.Column(db.DateTime(), nullable=False)

    def __init__(self, *args, **kwargs):
        for dictionary in args:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def object_as_dict(self):
        return {c: getattr(self, c) for c in ['payment_date', 'amount']}
