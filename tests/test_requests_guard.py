#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_requests_guard
----------------------------------

Tests for `requests-guard` module.
"""

import requests
import time
import unittest

from requests_guard import guard, guard_iter


class TestRequestsGuard(unittest.TestCase):
    def test_guard(self):
        r = requests.get("https://www.google.com/", stream=True, timeout=30)
        guard(r)

    def test_guard_iter(self):
        r = requests.get("https://www.google.com/", stream=True, timeout=30)
        for chunk in guard_iter(r):
            pass

    def test_size_limit(self):
        r = requests.get("https://www.google.com/", stream=True, timeout=1)
        with self.assertRaises(ValueError):
            for chunk in guard_iter(r, max_size=10):
                chunk

    def test_sleeping(self):
        r = requests.get("https://www.google.com/", stream=True, timeout=1)
        with self.assertRaises(ValueError):
            for chunk in guard_iter(r, timeout=1):
                time.sleep(2)

if __name__ == '__main__':
    unittest.main()
