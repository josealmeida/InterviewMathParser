from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "interview_math_parser"
default_task = "publish"


@init
def set_properties(project):
    project.version = "1.0"
    project.set_property('dir_source_main_python', 'interview_math_parser')
    project.set_property('dir_source_main_scripts', 'scripts')
    project.set_property('dir_source_unittest_python', 'tests')
    project.set_property('unittest_module_glob', 'test_*')
    project.depends_on_requirements("requirements.txt")
