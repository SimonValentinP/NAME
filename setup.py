try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'NAME',
    'author': 'Simon Poecheim',
    'url': 'https://github.com/SimonValentinP/',
    'download_url': 'https://github.com/SimonValentinP/NAME.git',
    'author_email': 'simon.poecheim@me.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)