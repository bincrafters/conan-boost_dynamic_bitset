from conans import ConanFile, tools, os

class BoostDynamic_BitsetConan(ConanFile):
    name = "Boost.Dynamic_Bitset"
    version = "1.65.1"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-dynamic_bitset"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["dynamic_bitset"]
    requires =  "Boost.Config/1.65.1@bincrafters/stable", \
                      "Boost.Core/1.65.1@bincrafters/stable", \
                      "Boost.Integer/1.65.1@bincrafters/stable", \
                      "Boost.Move/1.65.1@bincrafters/stable", \
                      "Boost.Serialization/1.65.1@bincrafters/stable", \
                      "Boost.Static_Assert/1.65.1@bincrafters/stable", \
                      "Boost.Throw_Exception/1.65.1@bincrafters/stable"

                      #config0 core2 integer3 move3 serialization11 static_assert1 throw_exception2
                      
    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()