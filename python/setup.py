
from setuptools import setup, find_packages

setup(
    name='dynamixel_sdk',
    version='3.6.0',
    packages=['dynamixel_sdk'],
    package_dir={'': 'src'},
    license='Apache 2.0',
    description='Dynamixel SDK 3. python package',
    long_description=open('README.txt').read(),
    url='https://github.com/ROBOTIS-GIT/DynamixelSDK',
    author='Leon Jung',
    author_email='rwjung@robotis.com',
    install_requires=['serial']
)