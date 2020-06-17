from setuptools import setup, find_packages

setup(
    name="pycli",
    description="A Python CLI Starter Template",
    version="0.1",
    author="Ryan Plyler <grplyler@liberty.edu>",
    packages=find_packages(),
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "pycli = pycli.cli:cli"
        ]
    },
)