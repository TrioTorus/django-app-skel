import os
from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


def get_readme():
    """Return the README file contents. Supports text,rst, and markdown"""
    for name in ('README', 'README.rst', 'README.md'):
        if os.path.exists(name):
            return read_file(name)
    return ''

# Use the docstring of the __init__ file to be the description
DESC = " ".join(__import__('app_name').__doc__.splitlines()).strip()

setup(
    name="app_name",
    version=__import__('app_name').get_version().replace(' ', '-'),
    url='https://bitbucket.org/dries/app_name', # TODO: check if this url is correct
    author='Dries Desmet', # TODO: fill in your name
    author_email='dries@urga.be', # TODO: fill in your e-mail address.
    description=DESC,
    long_description=get_readme(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_file('requirements.txt'),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Framework :: Django',
    ],
)
