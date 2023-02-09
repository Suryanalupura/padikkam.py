import os
from InvoiceGenerator.api import Client,Creator,Invoice,Provider,Item
from InvoiceGenerator.Pdf import simpleInvoice

os.environ["INVOICE_LANG"] = "en"

client= Client('Youtube')
provider = Provider('Youtube', bank_account= '123456789',bank_code='12345')
creator=Creator('justin singh')

invoice = Invoice(client,provider,creator)
invoice.currency_locale= 'en_USUTF-8'

invoice.add_item(Item(32,600, description='zxcv'))
invoice.add_item(Item(60,600, description='zxcv',tax=11))
invoice.add_item(Item(32,600, description='zxcv',tax=22))
invoice.add_item(Item(32,600, description='zxcv',tax=33))

pdf=simpleInvoice(invoice)
pdf.gen("invoice.pdf",generate_qr_code=True)
