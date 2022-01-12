#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


requirements = [ ]

with open('requirements.txt') as f:
    requirements += f.read().splitlines()

test_requirements = ['pytest>=3', ]

setup(
    author="Maxym Myroshnychenko",
    author_email='mmyros@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Statistical rethinking homework in Python and numpyro, class of 2022",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='statistical_rethinking_pyth_2022',
    name='statistical_rethinking_pyth_2022',
    packages=find_packages(include=['statistical_rethinking_pyth_2022', 'statistical_rethinking_pyth_2022.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/mmyros/statistical_rethinking_pyth_2022',
    version='0.1.0',
    zip_safe=False,
)
