from setuptools import setup, find_packages

setup(
    name='autobahn-autoreconnect',
    version='0.0.1',

    description='Python Autobahn runner with auto-reconnect feature',
    url='https://github.com/wegroupwolves/autobahn-autoreconnect',
    author='isra17',
    author_email='it@wegroup.be',
    license='LGPL2',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['autobahn>=0.14.0']
)
