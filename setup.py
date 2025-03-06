"""Setup script for the delta-313 project."""

from setuptools import find_packages, setup

setup(
    name="delta-313",
    version="0.1.0",
    description="Demo project with a CLI utility and data validation library",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pyyaml>=6.0.1",
        "rich>=13.9.4",
    ],
    extras_require={
        "dev": [
            "icecream>=2.1.3",
            "pytest>=8.3.4",
            "rich>=13.9.4",
            "textual>=1.0.0",
            "tqdm>=4.67.1",
        ],
        "cli": [
            "ruff",
            "pylint",
            "click>=8.1.7",
            "tqdm>=4.67.1",
        ],
    },
    python_requires=">=3.13",
    entry_points={
        "console_scripts": [
            "textutils=textkit.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
