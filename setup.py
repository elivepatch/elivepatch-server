from setuptools import setup, find_packages

setup(
    name='elivepatch_server',
    version='0.01',
    description='Distributed elivepatch server API',
    url='https://wiki.gentoo.org/wiki/User:Aliceinwire/elivepatch, ' + \
        'https://github.com/aliceinwire/elivepatch-server',
    author='Alice Ferrazzi',
    author_email='alice.ferrazzi@gmail.com',
    license='GNU GPLv2+',
    packages=find_packages(),
    scripts=['elivepatch-server'],
)
