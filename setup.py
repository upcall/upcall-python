# coding: utf-8

"""
    Upcall API

    A RESTful API (json) to manage your human-powered outbound call campaigns.

    OpenAPI spec version: 2
    Contact: support@upcall.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
from setuptools import setup, find_packages

NAME = "Upcall"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Upcall API",
    author_email="support@upcall.com",
    url="",
    keywords=["Swagger", "Upcall API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    A RESTful API (json) to manage your human-powered outbound call campaigns.
    """
)
