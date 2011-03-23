from django.db import models
from django.utils.hashcompat import md5_constructor

from signals import payment_was_successfull

class QuickpayTransaction(models.Model):
    msgtype = models.CharField(max_length=128)
    ordernumber = models.CharField(max_length=20)
    amount = models.PositiveIntegerField()
    currency = models.CharField(max_length=3)
    time = models.CharField(max_length=12)
    state = models.IntegerField()
    qpstat = models.CharField(max_length=3)
    qpstatmsg = models.CharField(max_length=512, blank=True)
    chstat = models.CharField(max_length=3)
    chstatmsg = models.CharField(max_length=512, blank=True)
    merchant = models.CharField(max_length=100)
    merchantemail = models.EmailField(max_length=256)
    transaction = models.CharField(max_length=32)
    cardtype = models.CharField(max_length=32, blank=True)
    cardnumber = models.CharField(max_length=32, blank=True)
    cardexpire = models.CharField(max_length=4, blank=True)
    fee = models.CharField(max_length=10, blank=True)
    md5check = models.CharField(max_length=32)

    def __init__(self, *args, **kwargs):
        self.secret = kwargs.pop('secret', None)
        super(QuickpayTransaction, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return self.ordernumber

    def save(self, *args, **kwargs):
        super(QuickpayTransaction, self).save(*args, **kwargs)

        md_input = ''.join((
            self.msgtype,
            self.ordernumber,
            str(self.amount),
            self.currency,
            self.time,
            str(self.state),
            self.qpstat,
            self.qpstatmsg,
            self.chstat,
            self.chstatmsg,
            self.merchant,
            self.merchantemail,
            self.transaction,
            self.cardtype,
            self.cardnumber,
            self.fee,
            self.secret,
        ))
        valid = md5_constructor(md_input).hexdigest() == self.md5check and self.qpstat == '000'
        if valid:
            payment_was_successfull.send(sender=self, ordernumber=self.ordernumber)
