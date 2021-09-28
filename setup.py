from setuptools import setup, find_packages

import myprogram.constants as constants

setup(
    name="myprogram",
    version=constants.VERSION,
    description="A simple python program",
    packages=find_packages(),

    install_requires=[
        "pandas",
        "flask",
    ],

    entry_points={
        'console_scripts': [
            'myprogram=myprogram.__main__:main',
        ],
    },
)
