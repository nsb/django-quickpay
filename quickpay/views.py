
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseBadRequest

from forms import QuickpayForm
from models import QuickpayTransaction

class BaseQuickpayCallback(object):

    def  __call__(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = QuickpayForm(request.POST, instance=QuickpayTransaction(secret=self.get_secret(request)))
            if form.is_valid():
                transaction = form.save()
                return HttpResponse()
        return HttpResponseBadRequest()

    def get_secret(self, request):
        raise NotImplementedError("Your %s class has not defined a get_secret() method, which is required." % self.__class__.__name__)