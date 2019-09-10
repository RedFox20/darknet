import mama

##
# Explore Mama docs at https://github.com/RedFox20/Mama
#
class darknet(mama.BuildTarget):

    workspace = 'build'

    def dependencies(self):
        if self.windows:
            self.add_git('pthread', 'https://github.com/RedFox20/pthread-win32.git')
        self.add_git('opencv', 'https://github.com/RedFox20/opencv.git')

    def configure(self):
        self.enable_cxx17()
        self.add_cmake_options(
            f"OpenCV_DIR={self.find_target('opencv').build_dir()}",
            'SELECT_OPENCV_MODULES=opencv_world',
            'BUILD_USELIB_TRACK=NO')

    def package(self):
        self.export_include('include', build_dir=True)
        self.export_libs('.', ['.dll', '.lib', '.so'])
        if self.linux:
            self.export_syslib('pthread')
