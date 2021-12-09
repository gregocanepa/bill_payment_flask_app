from bill_payment import db


class Payable(db.Model):
    __tablename__ = 'payable'
    bar_code = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    type = db.Column(db.String(length=200), nullable=False)
    description = db.Column(db.String(length=1024), nullable=True)
    due_date = db.Column(db.DateTime(), nullable=False)
    amount = db.Column(db.Float(), nullable=False)
    status = db.Column(db.String(length=200), nullable=False)

    def __init__(self, *args, **kwargs):
        for dictionary in args:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def object_as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
