from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gymasy/__init__.py
from gymasy import __version__ as version

setup(
	name="gymasy",
	version=version,
	description="Gym Management System",
	author="Ismail Tabtabai",
	author_email="ismail@tabtabai.org",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
