from setuptools import setup, find_packages
from setuptools.command.sdist import sdist as _sdist
from setuptools.command.bdist_wheel import bdist_wheel as _bdist_wheel

import os

invoked_dir = os.getcwd()

class CustomSdist(_sdist):
    def make_distribution(self):
        # Ensure the 'exts' folder is included in the tar archive
        self.filelist.files = [f for f in self.filelist.files if f.startswith('exts') or f in ['setup.py', 'pyproject.toml']]
        for root, dirs, files in os.walk('exts'):
            for file in files:
                self.filelist.files.append(os.path.join(root, file))
        super().make_distribution()

class CustomBdistWheel(_bdist_wheel):
    def run(self):
        # Create a dummy wheel file to satisfy the build process
        dist_dir = os.path.join(self.dist_dir, f"{self.distribution.get_name()}-{self.distribution.get_version()}-py3-none-any.whl")
        with open(dist_dir, 'w') as f:
            f.write('')
        print(f"Created dummy wheel file at {dist_dir}")
        # Call the original run method to ensure any other necessary steps are completed
        super().run()
        
        # Remove the dummy wheel file
        if os.path.exists(dist_dir):
            os.remove(dist_dir)
            print(f"Removed dummy wheel file at {dist_dir}")


setup(
    name="ansys-tools-omniverse",
    packages=find_packages(),
    cmdclass={
        'sdist': CustomSdist,
        'bdist_wheel': CustomBdistWheel,
    },
    include_package_data=True,
)