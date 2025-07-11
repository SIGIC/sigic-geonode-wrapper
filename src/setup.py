# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2018 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################
import os

from distutils.core import setup

from setuptools import find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name="sigic_geonode",
    version="4.0.0",
    author="",
    author_email="",
    description="sigic_geonode, based on GeoNode",
    long_description=(read("README.md")),
    # Full list of classifiers can be found at:
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 1 - Planning",
    ],
    license="GPL",
    keywords="sigic_geonode geonode django",
    url="https://github.com/sigic_geonode/sigic_geonode",
    packages=find_packages(),
    dependency_links=["git+https://github.com/GeoNode/geonode.git@4.4.x#egg=GeoNode"],
    include_package_data=True,
)
