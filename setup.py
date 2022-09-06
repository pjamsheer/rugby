from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in rugby/__init__.py
from rugby import __version__ as version

setup(
	name="rugby",
	version=version,
	description="Rugby is a frappe framework app for managing SCRUM projects",
	author="kuttypjamsheer@gmail.com",
	author_email="kuttypjamsheer@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
