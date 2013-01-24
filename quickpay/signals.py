from django.dispatch import Signal

payment_successful = Signal()
payment_failed = Signal()