from models import QuickpayTransaction
from django.views.generic.edit import BaseCreateView

class BaseQuickpayCallback(BaseCreateView):
	"""
	Base view for receiving Quickpay callbacks.
	"""
	http_method_names = ('post',)
	model = QuickpayTransaction