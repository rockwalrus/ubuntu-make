# -*- coding: utf-8 -*-
# Copyright (C) 2014 Canonical
#
# Authors:
#  Didier Roche
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; version 3.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA


"""Framework with another category module without any framework"""

import udtc.frameworks


class DCategory(udtc.frameworks.BaseCategory):

    def __init__(self):
        super().__init__(name="Category D", description="Category D description (empty has no installable framework)")


class FrameworkA(udtc.frameworks.BaseFramework):

    def __init__(self, category):
        super().__init__(name="Framework A", description="Description for framework A (restricted arch)",
                         category=category, only_on_archs=["foo", "baz"])

    def setup(self, install_path=None):
        super().setup(install_path=install_path)



class FrameworkB(udtc.frameworks.BaseFramework):

    def __init__(self, category):
        super().__init__(name="Framework B", description="Description for framework B (restricted version)",
                         category=category, only_ubuntu_version=["9.10", "10.04"])

    def setup(self, install_path=None):
        super().setup(install_path=install_path)


class FrameworkC(udtc.frameworks.BaseFramework):

    def __init__(self, category):
        super().__init__(name="Framework C", description="Description for framework C (restricted version and arch)",
                         category=category, only_on_archs=["foo", "bar", "baz"],
                         only_ubuntu_version=["9.10", "10.04", "10.10.10"])

    def setup(self, install_path=None):
        super().setup(install_path=install_path)