from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in asc_portal/__init__.py
from asc_portal import __version__ as version

setup(
	name="asc_portal",
	version=version,
	description="ASC Portal for website.",
	author="ASC 360",
	author_email="ramit.panangat@acube.co",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
