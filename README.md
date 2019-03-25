[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/payabbhi/payabbhi-python/blob/master/LICENSE)

# Payabbhi Python library

Make sure you have signed up for your [Payabbhi Account](https://payabbhi.com/docs/account) and downloaded the [API keys](https://payabbhi.com/docs/account/#api-keys) from the [Portal](https://payabbhi.com/portal).

## Requirements

Python 2.7 and later.

## pip

The library can be installed via [pip](https://pypi.python.org/). Run the following command:

```bash
$ pip install payabbhi
```

## Manual Installation

Download the library and install as below:

```py
python setup.py install
```

## Dependencies

The library requires the following extensions:

- [`requests`](http://docs.python-requests.org/en/master/)

If installed via setup.py, the dependencies are handled automatically. In case of manual installation,  make sure that the dependencies are resolved.

## Documentation

Please refer to:
- [Python Lib Docs](https://payabbhi.com/docs/api/?python)
- [Integration Guide](https://payabbhi.com/docs/integration)


## Getting Started

### Authentication

```py
import payabbhi
# Set your credentials
client = payabbhi.Client(access_id='<access_id>', secret_key='<secret_key>')

# Optionally set your app info.
# app_version and app_url are optional
client.set_app_info(app_name='app_name',
                    app_version='app_version',
                    app_url='app_url')
```

### Orders
```py
# Create order
order = client.order.create(data={'amount': 100,
                                  'merchant_order_id': 'ORD_001',
                                  'currency':'INR'})
```

### Verify a payment signature

```py
client.utility.verify_payment_signature({
        'order_id': '<order_id>',
        'payment_id': '<payment_id>',
        'payment_signature': '<payment_signature>'
})
```

### Verify webhook signature

```py
# replay_interval is optional. (default value is 300 seconds)
client.utility.verify_webhook_signature('<payload>','<actual_signature>','<secret>',<replay_interval>)
```

## Tests

Install dependencies to run unittests
  - [unittest2](https://pypi.org/project/unittest2/)
  - [responses](https://pypi.python.org/pypi/responses)

```bash
$ pip install unittest2 responses
```
or using `easy_install`

```bash
$ easy_install unittest2 responses
```
**N.B: make sure version of `six` must be atleast 1.10.0**

Now run the entire test suite using

```bash
$ python -m unittest2 discover
```

Or to run an individual test file:

```bash
$ python -m unittest2 discover -p test_payment.py
```

## Testing for different versions of Python

Payabbhi Python Library is compatible with Python 2.6+, Python 3.3+ . We should run these tests for all the supported versions . For local testing, we use [tox](http://tox.readthedocs.org/) to handle testing against different Python versions.

### Setting up tox

Install tox using `pip install tox` and then simply run `tox` from the project root. But to make tox work you will need an interpreter installed for each of the versions of python we test (see the envlist in tox.ini).  You can find these releases on [Python downloads page](https://www.python.org/download/releases).

You may choose not to install interpreters for every Python version we support. In that case, test at least any one of Python 2.x versions and any one of Python 3.x versions.

You can test with a specific interpreter e.g. Python 2.7 using `tox -e py27`.
