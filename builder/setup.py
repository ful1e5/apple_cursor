#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="applbuild",
    version="1.1.3",
    description="Generate 'macOSBigSur' cursor theme from PNGs file",
    url="https://github.com/ful1e5/apple_cursor",
    packages=["applbuild"],
    package_dir={"applbuild": "applbuild"},
    author="Kaiz Khatri",
    author_email="kaizmandhu@gamil.com",
    install_requires=["clickgen==1.1.8"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    python_requires=">=3.8",
    zip_safe=True,
)
