"""Setup script for the dataval package."""

from setuptools import find_packages, setup

setup(
    name="dataval",
    version="0.1.0",
    description="Data validation and transformation library",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pyyaml>=6.0.1",
    ],
    extras_require={
        "dev": [
            "pytest>=8.3.4",
            "rich>=13.9.4",
        ],
        "cli": [
            "ruff",
            "pylint",
        ],
    },
    python_requires=">=3.13",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)