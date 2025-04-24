import os 
from setuptools import setup, find_packages

cwd = os.path.dirname(os.path.abspath(__file__))

# Read requirements but filter out any lines starting with --
with open('requirements.txt') as f:
    reqs = [line.strip() for line in f.readlines() 
            if line.strip() and not line.startswith('--')]

setup(
    name='melotts',
    version='0.1.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=reqs,
    package_data={
        '': ['*.txt', 'cmudict_*'],  # Keep CMU dictionary files for English
    },
    entry_points={
        "console_scripts": [
            "melotts = melo.main:main",
            "melo = melo.main:main",
            "melo-ui = melo.app:main",
        ],
    },
)
