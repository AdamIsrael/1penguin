import os

from setuptools import setup

VERSION = "0.1"


def readme():
    """ Load the contents of the README file """
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    with open(readme_path, "r") as f:
        return f.read()


setup(
    name="1penguin",
    version=VERSION,
    author="Adam Israel",
    author_email="adam@adamisrael.com",
    description="An appindicator for accessing 1password credentials.",
    long_description=readme(),
    install_requires=[],
    license="",
    url="http://github.com/adamisrael/1penguin",
    classifiers=[],
    packages=["onepenguin"],
    # scripts=["bin/1penguin"],
    entry_points={
        'console_scripts': [
            '1penguin = onepenguin:main',
        ]
    },

    tests_require=["nose", "mock"],
    test_suite="nose.collector",
)
