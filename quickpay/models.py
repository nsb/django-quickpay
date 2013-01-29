from django.db import models
from hashlib import md5
from django.db.models.signals import post_save
from django.dispatch import receiver
import signals

class QuickpayTransaction(models.Model):
    msgtype = models.CharField(max_length=128)
    ordernumber = models.CharField(max_length=20)
    amount = models.PositiveIntegerField()
    currency = models.CharField(max_length=3)
    time = models.CharField(max_length=32)
    state = models.IntegerField()
    qpstat = models.CharField(max_length=3)
    qpstatmsg = models.CharField(max_length=512, null=True, blank=True)
    chstat = models.CharField(max_length=3)
    chstatmsg = models.CharField(max_length=512, null=True, blank=True)
    merchant = models.CharField(max_length=100)
    merchantemail = models.EmailField(max_length=256)
    transaction = models.CharField(max_length=32)
    cardtype = models.CharField(max_length=32, null=True, blank=True)
    cardnumber = models.CharField(max_length=32, null=True, blank=True)
    cardhash = models.CharField(max_length=53, null=True, blank=True)
    cardexpire = models.CharField(max_length=4, null=True, blank=True)
    splitpayment = models.IntegerField(null=True, blank=True)
    fraudprobability = models.CharField(max_length=10, null=True, blank=True)
    fraudremarks = models.CharField(max_length=512, null=True, blank=True)
    fraudreport = models.CharField(max_length=512, null=True, blank=True)
    fee = models.CharField(max_length=10, null=True, blank=True)
    md5check = models.CharField(max_length=32)

    def __unicode__(self):
        return self.ordernumber

    def is_success(self):
        return self.qpstat == '000'

    def is_fail(self):
        return not self.is_success()

    def is_valid(self, secret):
        md5data = (
            self.msgtype,
            self.ordernumber,
            self.amount,
            self.currency,
            self.time,
            self.state,
            self.qpstat,
            self.qpstatmsg,
            self.chstat,
            self.chstatmsg,
            self.merchant,
            self.merchantemail,
            self.transaction,
            self.cardtype,
            self.cardnumber,
            self.cardhash,
            self.cardexpire,
            self.splitpayment,
            self.fraudprobability,
            self.fraudremarks,
            self.fraudreport,
            self.fee,
            secret,
        )

        md5string = ''.join([str(val) for val in md5data if val is not None])
        return md5(md5string).hexdigest() == self.md5check

@receiver(post_save, sender=QuickpayTransaction, dispatch_uid='check_status')
def check_status(sender, instance, created, *a, **k):
    if not created:
        return
    elif instance.is_success():
        signals.payment_successful.send(sender=instance)
    else:
        signals.payment_failed.send(sender=instance)
