import sys

from setuptools import setup, find_packages

if not sys.version_info[0] == 3:
    print("only python3 supported!")
    sys.exit(1)

setup(
    name="vcsSHARK",
    version="2.1.1",
    author="Fabian Trautsch",
    author_email="trautsch@cs.uni-goettingen.de",
    description="vcsSHARK is a tool to analyze source code repositories",
    install_requires=[
        "mongoengine",
        "pygit2==0.26.2",
        "pymongo==3.12.2",
        "pycoshark>=1.2.6",
        "joblib",
    ],
    url="https://github.com/smartshark/vcsSHARK",
    download_url="https://github.com/smartshark/vcsSHARK/zipball/master",
    packages=find_packages(),
    entry_points={"console_scripts": ["vcsshark = pyvcsshark:start"]},
    test_suite="tests",
    zip_safe=False,
    include_package_data=True,
    package_data={
        "pyvcsshark": ["loggerConfiguration.json"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
