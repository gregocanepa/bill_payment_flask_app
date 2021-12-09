import click
from flask.cli import with_appcontext
from .extensions import db
from bill_payment.transactions.models import Transaction
from bill_payment.payables.models import Payable


@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()
