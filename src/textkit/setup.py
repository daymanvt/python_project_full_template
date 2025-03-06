"""Setup script for the texkit package."""

from setuptools import find_packages, setup

setup(
    name="texkit",
    version="0.1.0",
    description="Text utilities and processing library",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "rich>=13.9.4",
        "click>=8.1.7",
    ],
    extras_require={
        "dev": [
            "icecream>=2.1.3",
            "pytest>=8.3.4",
            "tqdm>=4.67.1",
        ],
    },
    python_requires=">=3.13",
    entry_points={
        "console_scripts": [
            "textutils=texkit.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)