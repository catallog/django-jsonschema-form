from setuptools import find_packages
from setuptools import setup

setup(
    author="Collabo Software Ltda",
    author_email="basask@collabo.com.br",
    description="Django admin widgets to render jsonschema as forms",
    name="django-jsonschema-form",
    long_description="Django admin widgets to render jsonschema as forms",
    version="1.0.3",
    url="https://www.collabo.com.br/",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    package_data={
        'jsonschemaform': ['templates/*.html', 'static/**/*.js'],
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
