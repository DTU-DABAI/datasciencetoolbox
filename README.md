[![Documentation Status](https://readthedocs.org/projects/datasciencetoolbox/badge/?version=latest)](https://datasciencetoolbox.readthedocs.io/en/latest/?badge=latest) [![Build Status](https://travis-ci.org/DTU-DABAI/datasciencetoolbox.svg?branch=master)](https://travis-ci.org/DTU-DABAI/datasciencetoolbox)

# The Data Science Tool Box
A simple collection of well documented methods for performing data science on a wide range of data.

![Under Construction](img/underconstruction.jpg)

# Project Structure / Naming convention
the toolbox contains methods for different tasks within different domains with the naming convention `datasciencetoolbox.<domain>.<task>.<method>`
the most important domain name is 'general' containing generic implementations of methods for fundamental tasks(i.e. implementation of a nearest-neighbor classifier).

"Domain name examples":

- General
- Time Series
- ...

Domains may use methods from other domains depending on how specialized they are. Most domains uses something from the general domain

"Task name examples":

- preprocessing
- modeling
- ...


# Contributing

Following these guidelines when contributing to the data science tool box


# Testing

Tests are located in the test directory and run by either

```
pytest
```
or to test the installation of the package with tox
```
tox
```
...
