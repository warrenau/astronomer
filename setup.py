from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent

VERSION = '1.1.4'
DESCRIPTION = 'constelation-astronomer: results processing package for CONSTELATION coupled model'
LONG_DESCRIPTION = (this_directory/ "README.md").read_text()

setup(
    name="constelation_astronomer",
    version=VERSION,
    author="Austin Warren",
    author_email="warrenau@oregonstate.edu",
    url="https://github.com/warrenau/astronomer",
    license="MIT License",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    py_modules=['astronomer'],
    install_requires=['numpy','matplotlib'],
    keywords=['python','data processing','Serpent 2', 'STAR-CCM+'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ]
)