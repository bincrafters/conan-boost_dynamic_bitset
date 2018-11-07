#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/stable")

class BoostDynamic_BitsetConan(base.BoostBaseConan):
    name = "boost_dynamic_bitset"
    url = "https://github.com/bincrafters/conan-boost_dynamic_bitset"
    lib_short_names = ["dynamic_bitset"]
    header_only_libs = ["dynamic_bitset"]
    b2_requires = [
        "boost_config",
        "boost_core",
        "boost_integer",
        "boost_move",
        "boost_serialization",
        "boost_static_assert",
        "boost_throw_exception"
    ]


