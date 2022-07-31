from distutils.core import setup

from Cython.Build import cythonize

setup(
    name="cyjpholiday",
    version="0.1.0",
    description="jpholiday Cython Package",
    long_description="jpholiday Cython Package",
    ext_modules=cythonize(
        [
            "jpholiday/jpholiday.pyx",
            "jpholiday/holiday.pyx",
            "jpholiday/holiday.pxd",
            "jpholiday/utils.pyx",
            "jpholiday/utils.pxd",
        ]
    ),
    maintainer="",
    maintainer_email="",
    zip_safe=False,
    include_package_data=False,
)
