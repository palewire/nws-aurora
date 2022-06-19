import os

from setuptools import setup


def read(file_name):
    this_dir = os.path.dirname(__file__)
    file_path = os.path.join(this_dir, file_name)
    with open(file_path) as f:
        return f.read()


setup(
    name="nws-aurora",
    version="0.0.1",
    description="Download forecast data for Aurora Borealis and Aurora Australis from the National Weather Service",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Ben Welsh",
    author_email="b@palewi.re",
    url="http://www.github.com/palewire/nws-aurora",
    license="MIT",
    packages=("nws_aurora",),
    entry_points="""
        [console_scripts]
        nwsaurora=nws_aurora.cli:cmd
    """,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
    project_urls={
        "Maintainer": "https://github.com/palewire",
        "Source": "https://github.com/palewire/nws-aurora",
        "Tracker": "https://github.com/palewire/nws-aurora/issues",
    },
)
