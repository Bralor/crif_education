#!/usr/bin/python3.8

from pprint import pprint

no_magic_methods = [
    method
    for method in dir(tuple)
    if not method.startswith("__")
]

pprint(no_magic_methods)

