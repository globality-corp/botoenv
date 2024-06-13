#!/usr/bin/env python
from setuptools import find_packages, setup


project = "botoenv"
version = "1.0.0"

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
        "botocore>=1.12.248",
    ],
    setup_requires=[
    ],
    dependency_links=[
    ],
    entry_points={
        "console_scripts": [
            "botoenv = botoenv.main:main"
        ],
    },
    extras_require={
        "test": [
            "pytest",
            "coverage>=4.0.3",
            "parameterized>=0.6.1",
            "mock>=1.0.1",
            "PyHamcrest>=1.9.0",
            "pytest-cov",
        ],
        "lint": [
            "flake8>=3.5.0",
            "flake8-isort>=3.0.1",
            "flake8-print>=3.1.0",
            "isort<5"
        ],
        "typehinting": [
            "mypy",
        ],
    },
)
