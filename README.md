#django-quickpay
###A Django app for danish payment gateway Quickpay

----

###Configuration

```python
INSTALLED_APPS = (
	...
	'quickpay'
)
```

`./manage.py syncdb`

----

###Models

`models.QuickpayTransaction`

```python

transaction = QuickpayTransaction

```

----

###Views

`views.BaseQuickpayCallback(BaseCreateView)`

```python
url(r'^quickpay/callback/$', views.BaseQuickpayCallback.as_view(), name='quickpay-callback')
```

----

###Forms


----