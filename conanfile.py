#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class LibnameConan(ConanFile):
    name = "snmp_pp"
    version = "3.3.12"
    description = "SNMP library"
    topics = ("snmp")
    url = "https://github.com/swissdotnet-sa/conan-snmp_pp"
    homepage = "https://github.com/swissdotnet-sa/snmp_pp"
    author = "Simon Lepasteur <simon.lepasteur@swissdotnet.ch>"
    license = "CC0-1.0"
    exports = ["LICENSE.md"]
    _source_subfolder = "source_subfolder"

    def configure(self):
        self.requires("OpenSSL/1.1.1a@conan/stable")

    def source(self):
        source_url = "https://github.com/swissdotnet-sa/snmp_pp"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.version), sha256="428a2a03a2c81d5a6a498ac0eca6243baaca18f90aa9c2eaf4e0ead095655755")
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self._source_subfolder)
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src=os.path.join(self._source_subfolder, "include"))
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["snmp++"]
