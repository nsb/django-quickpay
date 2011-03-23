=========================
django-quickpay
=========================

A Django app for danish payment gateway Quickpay

Configuration
==============

In order to use django-object-permissions you must:

 1. add the following to your django settings:

    * `Add 'quickpay' to INSTALLED_APPS`

 2. add the following to your url conf:

    * `(r'^payments/quickpay/callback/', 'quickpay_callback', {}, 'quickpay_callback')`

Usage
=====

Handle a successfull payment by connecting a handler to the payment_was_successfull signal::

    payment_was_successfull.connect(payment_handler)
