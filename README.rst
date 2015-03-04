===============================
Requests Guard
===============================

.. image:: https://img.shields.io/travis/skorokithakis/requests-guard.svg
        :target: https://travis-ci.org/skorokithakis/requests-guard

.. image:: https://img.shields.io/pypi/v/requests-guard.svg
        :target: https://pypi.python.org/pypi/requests-guard

.. image:: https://readthedocs.org/projects/requests-guard/badge/?version=latest
        :target: https://readthedocs.org/projects/requests-guard/?badge=latest
        :alt: Documentation Status

requests-guard is a small library that allows you to impose size and time limits on your HTTP requests.

* Free software: BSD license
* Documentation: https://requests-guard.readthedocs.org.

Features
--------

* Timeout limits
* Size limits
* Much more!

Installation
------------

Just use `pip` to install it:

```
pip install requests-guard
```

and you're done.

Usage
-----

```
import requests
from requests_guard import guard

r = requests.get("https://www.google.com/", stream=True, timeout=30)
content = guard(r, max_size=3000, timeout=10)
```

`requests-guard` will raise a `ValueError` if it receives more than `max_size` data in total, or if the *entire*
request takes more than `timeout` seconds to be completed. That means that the call will always return after (roughly,
see below for details) `timeout` seconds.

*Note:* You *must* call requests in the manner above, with `stream=True` and `timeout`. `stream=True` allows the size
and time limits to be set, and the `timeout` parameter to `requests` instructs it to close the connection if no data
has been received for that number of seconds.

*Note:* `requests-guard` works by looking at the data as it receives it, so the `timeout` parameter to `requests-guard`
will apply to the *entire* connection, not just the latest chunk. The `timeout` parameter to `requests` means "quit if
we haven't received any data for that long", which means that a response may take an arbitrary amount of time, as long
as it always returns *something* every `timeout` seconds. This means that a request may potentially take up to the sum
of the timeout specified to `requests` and to `requests-guard`, if the server stops replying completely just before
the timeout in `requests-guard` elapses.

