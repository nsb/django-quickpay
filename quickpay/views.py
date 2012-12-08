from django.http import HttpResponse, HttpResponseBadRequest
from models import QuickpayTransaction
from django.views.generic.edit import BaseCreateView

class BaseQuickpayCallback(BaseCreateView):
	"""
	Base view for receiving Quickpay callbacks.
	"""
	model = QuickpayTransaction