import math
import os
import sys

import requests

print(sys.version_info)
print(sys.executable)


def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting


print(greet('World'))
print(greet('Kevin'))
r = requests.get("http://cnn.com")
print(r.status_code)
