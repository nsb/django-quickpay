from django import forms
from django.conf import settings

from models import QuickpayTransaction


class QuickpayForm(forms.ModelForm):
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

    class Meta:
        model = QuickpayTransaction
        fields = ('msgtype', 'ordernumber', 'amount', 'currency', 'splitpayment', 'cardhash', 'md5check')
        widgets = {
            'msgtype': forms.HiddenInput,
            'ordernumber': forms.HiddenInput,
            'amount': forms.HiddenInput,
            'currency': forms.HiddenInput,
            'splitpayment': forms.HiddenInput,
            'cardhash': forms.HiddenInput,
            'md5check': forms.HiddenInput,
        }