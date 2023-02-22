from datetime import datetime, date
from pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item, Transaction
from pyinvoice.templates import SimpleInvoice

doc = SimpleInvoice('invoice.pdf')
#doc.is_paid = True


doc.invoice_info = InvoiceInfo(1023, datetime.now(), datetime.now())  

doc.service_provider_info = ServiceProviderInfo(
    name='kk bakers',
    street='Ramavarmapuram',
    city='Thrissur',
    state='kerala',
    post_code='123',
    
)

doc.client_info = ClientInfo(name= 'kk', email='kk@email.com')

doc.add_item(Item('puffs', '', 10, '15'))
doc.add_item(Item('sandwich', '', 10, '30'))
doc.add_item(Item('burgers', '', 10, '40'))

doc.set_item_tax_rate(20)  

doc.add_transaction(Transaction('Paypal', 111, datetime.now(), 300))
doc.add_transaction(Transaction('Stripe', 222, date.today(), 200))

doc.set_bottom_tip("Email: email@email.com<br />Thank you for shopping ")

doc.finish()
