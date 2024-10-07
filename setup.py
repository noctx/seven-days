#!/usr/bin/env python3
from setuptools import find_packages, setup

setup(name = 'seven_days',
    version = '1.0.0a0',
    description = "Polymorphic ransomware",
    platforms = ["Linux"],
    author="Nicolas Briant",
    author_email="n.briant6@gmail.com",
    url="https://gitlab.apolyon.eu/root/seven-days",
    license = "MIT",
    packages=find_packages()
    )
