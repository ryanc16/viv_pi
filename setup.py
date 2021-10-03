from setuptools import setup, find_packages

setup(
    name='viv-pi',
    version='0.1.0-alpha',
    description='A vivarium controller application for the Raspberry PI',
    packages=find_packages(exclude='tests'),
    include_package_data=True,
    install_requires=[
        'importlib; python_version == "3.7"',
    ],
)