import os
from setuptools import setup, find_packages


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='qventusdbschemas',
    version='0.0.1',
    license='MIT licence, see LICENCE.txt',
    description='schemas package contains all database scripts for initial setup',
    # long_description=(read('README.md')),
    ulr ='https://github.com/fahad0392/schema',
    author='Fahad Siddiqui',
    author_email='fahadsiddiqui707@gmail.com',
    include_package_data=True,
    packages = find_packages(),
)
