from setuptools import setup, find_packages

setup(
    name='simpleHKmodel',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        "numpy",
        "plotly",
        "IPython"
    ]
)