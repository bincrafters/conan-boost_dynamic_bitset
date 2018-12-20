#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostDynamic_BitsetConan(base.BoostBaseConan):
    name = "boost_dynamic_bitset"
    url = "https://github.com/bincrafters/conan-boost_dynamic_bitset"
    lib_short_names = ["dynamic_bitset"]
    header_only_libs = ["dynamic_bitset"]
    cycle_group = "boost_cycle_group_c"
    b2_requires = ["boost_cycle_group_c"]
