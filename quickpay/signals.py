from django.dispatch import Signal

payment_was_successfull = Signal(providing_args=["ordernumber",])