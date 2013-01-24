from models import QuickpayTransaction
from django.views.generic.edit import BaseCreateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

class BaseQuickpayCallback(BaseCreateView):
	"""
	Base view for receiving Quickpay callbacks.
	"""
	http_method_names = ('post',)
	model = QuickpayTransaction

	@method_decorator(csrf_exempt)
	def dispatch(self, *args, **kwargs):
		return super(BaseQuickpayCallback, self).dispatch(*args, **kwargs)

	def form_valid(self, form):
		form.save()
		return HttpResponse('OK')

	def form_invalid(self, form):
		return HttpResponse('FAIL', status=400)