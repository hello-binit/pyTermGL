from setuptools import Extension, setup, find_packages
from Cython.Build import cythonize
import numpy

with open("README.md", "rb") as f:
    long_description = f.read().decode("utf-8")

setup(
    name="termgl",
    description="TermGL wrapper in Cython",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.1.0",
    author="Wojciech Graj",
    url="https://github.com/wojciech-graj/pyTermGL",
    license="MIT",
    ext_modules=cythonize(
        [
            Extension(
                "termgl",
                sources=["termgl.pyx", "TermGL/src/termgl.c"],
                include_dirs=["TermGL/lib", numpy.get_include()],
                define_macros=[
                    ("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION"),
                    ("TERMGL3D", None),
                    ("TERMGLUTIL", None),
                ],
            )
        ],
        language_level=2
    ),
    packages=find_packages("termgl"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Multimedia :: Graphics :: 3D Rendering",
        "Topic :: Terminals",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: C",
        "Programming Language :: Cython",
    ],
    keywords="graphics terminal render rendering text ascii",
)
