import pathlib
from setuptools import setup

VERSION = "0.1.2"

with open('requirements.txt') as f:
    required = f.read().splitlines()

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="diffino",
    version=VERSION,
    packages=["diffino"],
    include_package_data=True,
    install_requires=required,
    entry_points={'console_scripts': ['diffino = diffino.cli:main']},
    author="BriteCore",
    description="Diffing tools for comparing datasets in CSV, XLSX and other formats",
    long_description=README,
    long_description_content_type="text/markdown",
    keywords="diffing comparing csv excel json",
    url="https://github.com/IntuitiveWebSolutions/diffino"
)
