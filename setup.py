from setuptools import setup, find_packages

setup(
    name='netflix_stocks',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'pandas',
        'numpy',
        'yfinance',
        'plotly',
        'statsmodels',
    ],
)
