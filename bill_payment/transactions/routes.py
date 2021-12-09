import pandas as pd
# project import
from bill_payment import db, app
# models
from .models import Transaction
from bill_payment.payables.models import Payable
# flask imports
from flask import request
from flask import Response
from bill_payment.utils import string_to_datetime


@app.route('/insert_transaction', methods=['POST'])
def insert_transaction():
    json_transaction = request.get_json()
    bill_query = db.session.query(Payable).filter(Payable.bar_code == json_transaction['bar_code'])
    bill = bill_query.first()
    if bill is None:
        return Response("{'message': 'The bill doesnt exist.'}", status=400)
    if bill.status == "paid":
        return Response("{'message': 'This bill has already been paid.'}", status=400)

    json_transaction['payment_date'] = string_to_datetime(json_transaction['payment_date'])
    if json_transaction['payment_date'] > bill.due_date:
        return Response("{'message': 'The bill has expired.'}", status=400)

    bill_update = {'bar_code': json_transaction['bar_code'], 'status': 'paid'}
    bill_query.update(bill_update)
    transaction = Transaction(json_transaction)
    db.session.add(transaction)
    db.session.commit()
    return Response("{'message': 'The transaction has been created sucessfully.'}", status=201)


@app.route('/get_transactions', methods=['POST'])
def get_transactions():
    json_filters = request.get_json()
    from_date = string_to_datetime(json_filters['from_date'])
    to_date = string_to_datetime(json_filters['to_date'])
    transactions = db.session.query(Transaction).filter(
        Transaction.payment_date >= from_date,
        Transaction.payment_date <= to_date
    )
    df_transactions = pd.read_sql(transactions.statement, transactions.session.bind)
    transaction_groups = df_transactions.groupby('payment_date')
    transaction_group_list = []
    for group in transaction_groups.groups:
        group_df = transaction_groups.get_group(group)
        group_dict = {
            'total_amount': group_df['amount'].sum(),
            'total_transactions': len(group_df),
            'payment_date': group
        }
        transaction_group_list.append(group_dict)
    return {'transactions': transaction_group_list}
