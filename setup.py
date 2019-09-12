#!/usr/bin/env python3

import setuptools  # type: ignore

META = dict(
    name="onset",
    version="1.1.0",
    description="Run set operations on files.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fmind/onset",
    author="Médéric Hurier (fmind)",
    author_email="fmind@fmind.me",
    license="LGPL-3.0",
    packages=["onset"],
    keywords="set file utility operation",
    classifiers=["Development Status :: 4 - Beta"],
    entry_points={"console_scripts": ["onset=onset.__main__:main"]},
    python_requires=">=3.7",
    install_requires=[],
)

if __name__ == "__main__":
    setuptools.setup(**META)
