"""Installation file for the ansys-api-pyensight package"""

from datetime import datetime
import os
import shutil

import setuptools
import setuptools.command.build
import setuptools.command.build_py
from setuptools.command.build_py import build_py as build_py_orig
import setuptools.command.sdist

# Get the long description from the README file
HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(
    os.path.join(HERE, "src", "ansys", "tools", "omniverse", "VERSION"),
    encoding="utf-8",
) as f:
    version = f.read().strip()

package_name = "ansys-tools-omniverse"
description = f"An extension to send data to Omniverse using Ansys EnSight, built on {datetime.now().strftime('%H:%M:%S on %d %B %Y')}"


class CustomBuildPy(build_py_orig):
    def run(self):
        # Copy the exts folder to the desired package location
        target_dir = os.path.join(self.build_lib, "ansys", "tools", "omniverse", "exts")
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        exts = os.path.join(os.path.dirname(__file__), "exts")
        for item in os.listdir(exts):
            s = os.path.join(exts, item)
            d = os.path.join(target_dir, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
        super().run()


egg_info_dir = "build/egg-info"
if not os.path.exists(egg_info_dir):
    os.makedirs(egg_info_dir)


def package_files(directory):
    paths = []
    for path, directories, filenames in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join(path, filename))
    return paths


exts_files = package_files(os.path.join(os.path.dirname(__file__), "exts"))


_packages = setuptools.find_namespace_packages("src", include=("ansys.*",))

if __name__ == "__main__":
    setuptools.setup(
        name=package_name,
        version=version,
        author="ANSYS, Inc.",
        author_email="pyansys.core@ansys.com",
        maintainer="ANSYS, Inc.",
        maintainer_email="pyansys.core@ansys.com",
        description=description,
        long_description=long_description,
        long_description_content_type="text/markdown",
        url=f"https://github.com/ansys-internal/{package_name}",
        license="MIT",
        python_requires="~=3.10",
        package_dir={"": "src"},
        packages=_packages,
        cmdclass={"build_py": CustomBuildPy},
        include_package_data=True,
        package_data={"": ["VERSION"], "ansys.tools.omniverse": exts_files},
    )
