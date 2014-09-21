from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='forecastio-python-wrapper',
    version='2014.08a1',
    description='A Python wrapper for the http://forecast.io REST API.',
    long_description=long_description,
    url='https://github.com/LyleScott/forecastio-python-wrapper',
    author='Lyle Scott, III',
    author_email='lyle@digitalfoo.net',
    license='MIT',
    classifiers=[  # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='forecastio rest api',
    packages=find_packages(exclude=['tests', 'example']),
    install_requires=['requests'],
)
