from django import forms
from django.conf import settings

from models import QuickpayTransaction

class QuickpayForm(forms.ModelForm):
    """
    """
    protocol = forms.IntegerField(widget=forms.HiddenInput, required=False, initial=3)
    msgtype = forms.CharField(widget=forms.HiddenInput, initial='authorize',)
    language = forms.CharField(initial=settings.LANGUAGE_CODE, required=False, widget=forms.HiddenInput)
    autocapture = forms.IntegerField(initial=0, required=False, widget=forms.HiddenInput)
    cardtypelock = forms.CharField(
        widget=forms.HiddenInput,
        required=False,
        initial = "3d-jcb,3d-mastercard,3d-mastercard-dk,3d-visa,3d-visa-dk,american-express," \
                  "american-express-dk,dankort,diners,diners-dk,jcb,mastercard,mastercard-dk,visa,visa-dk"
    )
    ordernumber = forms.CharField(widget=forms.HiddenInput,)
    amount = forms.CharField(widget=forms.HiddenInput, initial=0)
    currency = forms.CharField(widget=forms.HiddenInput)
    merchant = forms.CharField(widget=forms.HiddenInput)
    continueurl = forms.URLField(widget=forms.HiddenInput, required=False)
    cancelurl = forms.URLField(widget=forms.HiddenInput, required=False)
    callbackurl = forms.URLField(required=False, widget=forms.HiddenInput)
    md5check = forms.CharField(widget=forms.HiddenInput)
    state = forms.IntegerField(widget=forms.HiddenInput)
    time = forms.CharField(widget=forms.HiddenInput, required=False)
    qpstat = forms.CharField(widget=forms.HiddenInput)
    qpstatmsg = forms.CharField(widget=forms.HiddenInput, required=False)
    chstat = forms.CharField(widget=forms.HiddenInput)
    chstatmsg = forms.CharField(widget=forms.HiddenInput, required=False)
    merchantemail = forms.EmailField(widget=forms.HiddenInput)
    cardtype = forms.CharField(widget=forms.HiddenInput)
    cardnumber = forms.CharField(widget=forms.HiddenInput, required=False)
    cardexpire = forms.CharField(widget=forms.HiddenInput, required=False)
    transaction = forms.CharField(widget=forms.HiddenInput)
    description = forms.CharField(widget=forms.HiddenInput, required=False)
    fee = forms.CharField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = QuickpayTransaction
