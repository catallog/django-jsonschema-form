from setuptools import find_packages
from setuptools import setup

import os
import codecs


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding="utf-8") as fp:
        return fp.read()

install_requires = open('requirements.txt').read().split('\n')

setup(
    author="Collabo Software Ltda",
    author_email="basask@collabo.com.br",
    description="Django admin widgets to render jsonschema as forms",
    name="django-jsonschema-form",
    long_description=read("README.md"),
    version="1.0.0",
    url="https://www.collabo.com.br/",
    license="MIT",
    packages=find_packages(),
    install_requires=install_requires,
    package_data={
        'jsonschemaform': ['templates/*.html', 'static/**/*.js']
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
