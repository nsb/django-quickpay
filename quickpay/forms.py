from django import forms
from django.conf import settings

class QuickpayForm(forms.Form):
    protocol = forms.IntegerField(widget=forms.HiddenInput, initial=6)
    language = forms.CharField(widget=forms.HiddenInput, initial=settings.LANGUAGE_CODE)
    cardtypelock = forms.CharField(widget=forms.HiddenInput, initial='creditcard')
    merchant = forms.CharField(widget=forms.HiddenInput)
    description = forms.CharField(widget=forms.HiddenInput)
    continueurl = forms.URLField(widget=forms.HiddenInput)
    cancelurl = forms.URLField(widget=forms.HiddenInput)
    callbackurl = forms.URLField(widget=forms.HiddenInput)
    autocapture = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    autofee = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    group = forms.IntegerField(widget=forms.HiddenInput)
    testmode = forms.IntegerField(widget=forms.HiddenInput, initial=int(settings.DEBUG))
    forcemobile = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    deadline = forms.IntegerField(widget=forms.HiddenInput)

    msgtype = forms.IntegerField(widget=forms.HiddenInput, initial='authorize')
    ordernumber = forms.CharField(widget=forms.HiddenInput)
    amount = forms.IntegerField(widget=forms.HiddenInput)
    currency = forms.CharField(widget=forms.HiddenInput, initial='USD')
    splitpayment = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    cardhash = forms.IntegerField(widget=forms.HiddenInput, initial=1)
    md5check = forms.CharField(widget=forms.HiddenInput)