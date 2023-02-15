from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="lda-arun-s-01",
    version="0.1",
    author="Arun S",
    author_email="a2r0u0n2@gmail.com",
    description="A small package for Dimensionality reduction using LDA",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ARUN-S01/lda",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)