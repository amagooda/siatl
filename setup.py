# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
from setuptools import setup

with open('requirements.txt') as fp:
    REQUIRES = fp.read()

root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root, "siatl", "about.py")) as f:
    package_info = {}
    info = f.read()
    exec(info, package_info)

setup(
    name=package_info["__title__"],
    version=package_info["__version__"],
    url=package_info["__uri__"],
    author=package_info["__author__"],
    description=package_info["__description__"],
    long_description=package_info["__summary__"],
    license=package_info["__license__"],
    packages=[
        "siatl.models",
        "siatl.logger", 
        "siatl.modules", 
        "siatl.utils"
        ],
    install_requires=REQUIRES,
    dependency_links=['https://github.com/pytorch/pytorch'],
    include_package_data=True
)
