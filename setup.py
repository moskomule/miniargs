from pathlib import Path

import setuptools

with (Path(__file__).parent / "README.md").open() as f:
    long_description = f.read()

setuptools.setup(name="miniargs",
                 version="0.2.0",
                 description="a simple argument parser",
                 long_description=long_description,
                 long_description_content_type='text/markdown',
                 author="Ryuichiro Hataya",
                 author_email="hataya@nlab.jp",
                 python_requires=">=3.6.0",
                 url="https://github.com/moskomule/miniargs",
                 packages=setuptools.find_packages(exclude=["test"]),
                 license="MIT",
                 classifiers=["License :: OSI Approved :: MIT License",
                              "Programming Language :: Python :: 3.6",
                              "Programming Language :: Python :: 3.7"]
                 )
