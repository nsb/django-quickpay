from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^callback/$', views.BaseQuickpayCallback.as_view(), name='quickpay_callback'),
)
