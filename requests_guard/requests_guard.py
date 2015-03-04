# -*- coding: utf-8 -*-

import time


def guard_iter(response, max_size=1 * 1024 ** 2, timeout=30):
    response.raise_for_status()

    if int(response.headers.get('Content-Length', "0")) > max_size:
        response.close()
        raise ValueError('Response too large.')

    size = 0
    start = time.time()

    for chunk in response.iter_content(1024):
        size += len(chunk)
        if size > max_size:
            response.close()
            raise ValueError('Response too large.')

        if time.time() - start > timeout:
            response.close()
            raise ValueError("Timeout reached.")

        yield chunk


def guard(response, max_size=1 * 1024 ** 2, timeout=30):
    b"".join(guard_iter(response, max_size, timeout))
