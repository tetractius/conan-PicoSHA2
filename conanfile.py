from conans import ConanFile, CMake, tools
import shutil
import os


class PicoSHA2Conan(ConanFile):
    name = "PicoSHA2"
    version = "1.0.0"
    license = "MIT"
    url = "https://github.com/okdshin/PicoSHA2"
    description = "A header-file-only, SHA256 hash generator in C++"
    no_copy_source = True
    homepage = "https://github.com/okdshin/PicoSHA2"
    # No settings/options are necessary, this is header only

    def source(self):
        tools.get("https://github.com/okdshin/PicoSHA2/archive/v{0}.zip".format(self.version))
        shutil.move("PicoSHA2-{0}".format(self.version), "sources")

    def package(self):
        self.copy(pattern="*.h*", dst="include", src="sources", keep_path=False)

    def package_info(self):
        self.cpp_info.includedirs = ["include"]
