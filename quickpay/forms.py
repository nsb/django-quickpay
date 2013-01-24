from django import forms
from django.conf import settings
from utils import request_md5check

class QuickpayForm(forms.Form):
    protocol = forms.IntegerField(widget=forms.HiddenInput, initial=6)
    msgtype = forms.IntegerField(widget=forms.HiddenInput, initial='authorize')
    merchant = forms.CharField(widget=forms.HiddenInput)
    language = forms.CharField(widget=forms.HiddenInput, initial=settings.LANGUAGE_CODE)
    ordernumber = forms.CharField(widget=forms.HiddenInput)
    amount = forms.IntegerField(widget=forms.HiddenInput)
    currency = forms.CharField(widget=forms.HiddenInput, initial='USD')
    continueurl = forms.URLField(widget=forms.HiddenInput)
    cancelurl = forms.URLField(widget=forms.HiddenInput)

    callbackurl = forms.URLField(widget=forms.HiddenInput, required=False)
    autocapture = forms.IntegerField(widget=forms.HiddenInput, required=False)
    autofee = forms.IntegerField(widget=forms.HiddenInput, required=False)
    cardtypelock = forms.CharField(widget=forms.HiddenInput, required=False)
    description = forms.CharField(widget=forms.HiddenInput, required=False)
    group = forms.IntegerField(widget=forms.HiddenInput, required=False)
    testmode = forms.IntegerField(widget=forms.HiddenInput, initial=int(settings.DEBUG), required=False)
    splitpayment = forms.IntegerField(widget=forms.HiddenInput, required=False)
    forcemobile = forms.IntegerField(widget=forms.HiddenInput, required=False)
    deadline = forms.IntegerField(widget=forms.HiddenInput, required=False)
    cardhash = forms.IntegerField(widget=forms.HiddenInput, required=False)

    md5check = forms.CharField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        secret = kwargs.pop('secret', None)
        super(QuickpayForm, self).__init__(*args, **kwargs)

        if secret:
            self.compute_md5check(secret)

    def compute_md5check(self, secret):
        data = {}

        for field in self:
            data[field.name] = field.value()

        self.fields['md5check'].initial = request_md5check(data, secret)