#!/usr/bin/env python
from setuptools import find_packages, setup

project = "botoenv"
version = "0.2.0"

setup(
    name=project,
    version=version,
    description="Manage AWS environment variables using botocore",
    author="Globality Engineering",
    author_email="engineering@globality.com",
    url="https://github.com/globality-corp/botoenv",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "botocore>=1.5.35",
    ],
    setup_requires=[
        "nose>=1.3.6",
    ],
    dependency_links=[
    ],
    entry_points={
        "console_scripts": [
            "botoenv = botoenv.main:main"
        ],
    },
    tests_require=[
        "coverage>=3.7.1",
        "mock>=1.0.1",
        "PyHamcrest>=1.8.5",
    ],
)
