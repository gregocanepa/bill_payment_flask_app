# project import
from bill_payment import db, app
# models
from .models import Payable
# flask imports
from flask import request
from flask import Response
from bill_payment.utils import string_to_datetime


@app.route('/insert_payable', methods=['POST'])
def insert_payable():
    json_payable = request.get_json()
    json_payable['due_date'] = string_to_datetime(json_payable['due_date'])
    payable = Payable(json_payable)
    db.session.add(payable)
    db.session.commit()
    return Response("{'message': 'The payable has been created sucessfully.'}", status=201)


@app.route('/get_payables', methods=['POST'])
def get_payables():
    json_payable = request.get_json()
    json_payable['status'] = 'pending'
    payables = db.session.query(Payable).filter_by(**json_payable)
    list_payables = []
    if json_payable:
        for payable in payables:
            payable_dict = payable.object_as_dict()
            del payable_dict["type"]
            list_payables.append(payable_dict)
    else:
        list_payables = [payable.object_as_dict() for payable in payables]
    return {'payables': list_payables}
