#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class SnmpPPConan(ConanFile):
    name = "snmp_pp"
    version = "3.3.13"
    description = "SNMP library"
    topics = ("snmp")
    url = "https://github.com/swissdotnet-sa/conan-snmp_pp"
    homepage = "https://github.com/swissdotnet-sa/snmp_pp"
    author = "Simon Lepasteur <simon.lepasteur@swissdotnet.ch>"
    license = "mit"
    exports = ["LICENSE"]
    _source_subfolder = "source_subfolder"

    def configure(self):
        self.requires("OpenSSL/1.1.1a@conan/stable")

    def source(self):
        source_url = "https://github.com/swissdotnet-sa/snmp_pp"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.version), sha256="67c6310cdd219966b63a2ab1522d820bccdebbdb6f2b69f25002a0291f98ddbf")
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
        self.cpp_info.libs = ["snmp_pp"]
