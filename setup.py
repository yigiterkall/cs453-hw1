#!/usr/bin/env python
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(
    # TODO: Write a globally unique name which will be listed on PyPI
    name="yigiterkall/cs453-hw1",
    author="Yigit Erkal",  # TODO: Write your name
    version="2.0.0",
    description="basic",
    packages=find_packages(),
    install_requires=[
        "requests>=2.23.0",
    ],
    python_requires=">=3.8",
    

)
