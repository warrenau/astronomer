from setuptools import setup, find_packages

VERSION = '0.2.0'
DESCRIPTION = 'constelation-astronomer: results processing package'
LONG_DESCRIPTION = 'constelation-astronomer: results processing package for CONSTELATION coupled model'

setup(
    name="constelation_astronomer",
    version=VERSION,
    author="Austin Warren",
    author_email="warrenau@oregonstate.edu",
    url="https://github.com/warrenau/astronomer",
    license="MIT License",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
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