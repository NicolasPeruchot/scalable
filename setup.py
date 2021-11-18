"""Manage dependencies."""
import pathlib

from setuptools import find_packages, setup


def _read(fname: str) -> str:
    with open(pathlib.Path(fname)) as fh:
        data = fh.read()
    return data


base_packages = [
    "numpy==1.21.3",
    "pandas==1.3.4",
    "seaborn==0.11.2",
    "matplotlib==3.4.3",
    "networkx==2.6.3",
    "scikit-learn==1.0.1",
]

dev_packages = [
    "black==21.10b0",
    "darglint==1.4.0",
    "flake8>=3.9.2",
    "flake8-bandit>=2.1.2",
    "flake8-annotations>=2.7.0",
    "flake8-bugbear>=21.9.2",
    "flake8-docstrings>=1.6.0",
    "ipykernel==6.5.0",
    "isort>=5.10.0",
    "pre-commit==2.15.0",
]


test_packages = [
    "pytest>=6.2.5",
]


setup(
    name="scalable",
    version="0.0.1",
    packages=find_packages(exclude=["notebooks", "tests"]),
    long_description=_read("README.md"),
    install_requires=base_packages,
    extras_require={"dev": dev_packages + test_packages, "test": test_packages},
)
