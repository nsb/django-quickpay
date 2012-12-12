from django.utils.hashcompat import md5_constructor as md5

def request_md5check(data, secret):
    """
    Computes the MD5 signature for a quickpay request.
    """

    md5pieces = (
        data['protocol'],
        data['msgtype'],
        data['merchant'],
        data['language'],
        data['ordernumber'],
        data['amount'],
        data['currency'],
        data['continueurl'],
        data['cancelurl'],

        data.get('callbackurl') or '',
        data.get('autocapture') or '',
        data.get('autofee') or '',
        data.get('cardtypelock') or '',
        data.get('description') or '',
        data.get('group') or '',
        data.get('testmode') or '',
        data.get('splitpayment') or '',
        data.get('forcemobile') or '',
        data.get('deadline') or '',
        data.get('cardhash') or '',

        secret
    )

    md5string = ''.join([str(val) for val in md5pieces])
    return md5(md5string).hexdigest()

