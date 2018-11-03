#!/usr/bin/env python

import os
import glob
import setuptools  # type: ignore

root = os.path.abspath(os.path.dirname(__file__))


def requires(requirements="requirements.txt"):
    path = os.path.join(root, requirements)

    with open(path, "r") as f:
        return f.read().splitlines()


info = dict(
    name="onset",
    version="1.0.11",
    license="EUPL-1.2",
    author="Médéric Hurier",
    author_email="dev@fmind.me",
    description="Run set operations on files.",
    long_description_content_type="text/markdown",
    long_description=open("README.md", "r").read(),
    url="https://git.fmind.me/fmind/onset",
    packages=["onset", "onset.scripts"],
    package_dir={"onset.scripts": "scripts"},
    keywords="set file utility operation",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
    ],
    extras_require={
        os.path.dirname(f): requires(f) for f in glob.glob("*/requirements.txt")
    },
    python_requires=">=3",
    install_requires=requires(),
    entry_points={"console_scripts": ["onset=onset.scripts.console:main"]},
)

if __name__ == "__main__":
    setuptools.setup(**info)
