from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Craps Simulator',
    version='0.1.0',
    description='Run a simulation of craps',
    long_description=readme,
    author='Bill Guedel',
    author_email='wsguede@gmail.com',
    url='https://github.com/wsguede/crapsSimulator',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)


# Learn more: https://github.com/kennethreitz/setup.py
