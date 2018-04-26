from setuptools import setup, find_packages

setup(
    name='hmlstm',
    version='0.0.1',
    description='Implementation of hierarchical multiscale hlstm network',
    url='https://github.com/n-s-f/hierarchical-rnn',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples']),
    install_requires=[
        "numpy",
        "matplotlib",
        "ruamel.yaml"
    ],
    extras_require={'tensorflow': ['tensorflow'],
                    'tensorflow with gpu': ['tensorflow-gpu']},
)
