from setuptools import setup, find_packages
import os

long_description = ""
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

setup(
    name="setlogo",
    version="1.0.0",
    author="ShawponSp",
    author_email="blackspammerbd@gmail.com",
    description="Professional Termux Fish Shell & Custom Banner Setup Tool by Black Spammer Bd.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Shawpon2/setlogo",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Terminals :: Terminal Emulators/X Terminals",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "setlogo=setlogo.cli:main",
        ],
    },
)
