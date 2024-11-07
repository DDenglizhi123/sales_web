from flask import Blueprint, render_template
# from models import *
from datetime import datetime

blue = Blueprint('user', __name__)



@blue.route('/cover_letter/')
def cover_letter():
    now=datetime.now()
    date = now.strftime("%d/%m/%Y")
    contract_number='PA/01/22-23/HQ/G/150'
    client_name='TANZANIA ELECTRIC SUPPLY CO. LTD (TANESCO)'
    pobox_number='63'
    address_1='KILIMANJARO'
    address_2='TANZANIA'
    address_3=''
    region_name1='KILIMANJARO'
    lpo_number='2000044633-1'
    commercial_invoice_number='EC202409-KILI-05'


    return render_template('cover_letter.html',
                           date=date,
                           contract_number=contract_number,
                           client_name=client_name,
                           pobox_number=pobox_number,
                           address_1=address_1,
                           address_2=address_2,
                           address_3=address_3,
                           region_name1=region_name1,
                           lpo_number=lpo_number,
                           commercial_invoice_number=commercial_invoice_number
                           )
@blue.route('/commercial_invoice/')
def commercial_invoice():
    return render_template('commercial_invoice.html')
@blue.route('/warranty')
def warranty():

    return render_template('warranty.html')
@blue.route('/insert_order', methods=['GET', 'POST'])
def insert_order():
    client_name='TANZANIA'
    tin_number='KILIMANJARO'
    vrn_number='EC202409-KILI-05'
    address_1='KILIMANJARO'
    address_2='TANZANIA'
    address_3=''
    contact_name='TANZANIA'
    contact_number='KILIMANJARO'
    email_address='<EMAIL>'
@blue.route('/daily_order', methods=['GET', 'POST'])
def daily_order():
    pass
@blue.route('/quote', methods=['GET', 'POST'])
def quote():
    pass
@blue.route('/template')
def template():
    return render_template('template.html')