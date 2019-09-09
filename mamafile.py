import mama

##
# Explore Mama docs at https://github.com/RedFox20/Mama
#
class darknet(mama.BuildTarget):

    workspace = 'build'

    def dependencies(self):
        self.add_git('opencv', 'https://github.com/RedFox20/opencv.git')

    def configure(self):
        self.enable_cxx17()
        self.add_cmake_options(
            f"OpenCV_DIR={self.find_target('opencv').build_dir()}",
            'SELECT_OPENCV_MODULES=opencv_world',
            'BUILD_USELIB_TRACK=NO')

    def package(self):
        self.export_include('include')
        self.export_libs('.', ['.dll', '.lib', '.so'])
