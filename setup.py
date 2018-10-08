from setuptools import setup

with open('LONG_DESCRIPTION.rst') as f:
    long_description = f.read()

setup(
    name="payabbhi",
    version="1.0.2",
    description="Payabbhi Python package provides client library for Payabbhi API's",
    long_description=long_description,
    url="https://github.com/payabbhi/payabbhi-python",
    author="Team Payabbhi",
    author_email="support@payabbhi.com",
    license="MIT",
    install_requires=["requests"],
    package_dir={'payabbhi': 'payabbhi', 'payabbhi.resources': 'payabbhi/resources', 'payabbhi.utility': 'payabbhi/utility'},
    packages=['payabbhi', 'payabbhi.resources', 'payabbhi.test', 'payabbhi.utility'],
    test_suite='payabbhi.test.all',
    tests_require=['unittest2', 'responses'],
    keywords='payabbhi payment processing api checkout india',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ]
)
