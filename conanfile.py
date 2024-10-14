from conan import ConanFile

class ConanPackage(ConanFile):
    name = 'starter-code'
    version = "0.1.0"

    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        self.requires("protobuf/5.27.0")
        # self.requires("boost/1.82.0")
        

    def build_requirements(self):
        self.tool_requires("cmake/3.22.6")
    
    # def configure(self):
    #     self.options["boost"].shared = False