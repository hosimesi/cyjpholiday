import os

from Cython.Build import cythonize
from setuptools import Extension, find_packages, setup

ext_modules = [
    Extension(
        "cyjpholiday.cyjpholiday",
        extra_compile_args=["-Wall", "-O3", "-std=c++0x", "-march=native", "-DUSESSE"],
        sources=[
            os.path.join("cyjpholiday", "cyjpholiday.pyx"),
            os.path.join("cyjpholiday", "holiday.pyx"),
            os.path.join("cyjpholiday", "holiday.pxd"),
            os.path.join("cyjpholiday", "utils.pyx"),
            os.path.join("cyjpholiday", "utils.pxd"),
        ],
        language="c++",
    )
]

if cythonize is not None:
    ext_modules = cythonize(ext_modules)


setup(
    name="cyjpholiday",
    version="0.1.0",
    description="jpholiday Cython Package",
    long_description="jpholiday Cython Package",
    ext_modules=ext_modules,
    install_requires=["calender", "datetime", "math"],
    maintainer="",
    maintainer_email="",
    zip_safe=False,
    packages=find_packages(exclude=("tests")),
    include_package_data=False,
    data_files=[
        ("cyjpholiday", ["holiday.pyx", "holiday.pxd", "utils.pyx", "utils.pxd"])
    ],
    package_data={"cyjpholiday": ["*.c", "*.cpp", "*.pyx", "*.pxd"]},
)
