from django.conf.urls.defaults import *

urlpatterns = patterns('quickpay.views',
    (r'^$', 'callback', {}, 'quickpay_callback',),
)
