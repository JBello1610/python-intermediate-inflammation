# Inflam
![Continuous Integration build in GitHub Actions](https://github.com/JBello1610/python-intermediate-inflammation/workflows/CI/badge.svg?branch=main)

Inflam is a data management system written in Python that manages trial data used in clinical inflammation studies.

## Main Features
Here are some  key features of Inflam:

- Provide basic statistical analyses over clinical trial data
- Ability ti woek on trial data in Comma0-Seperated Value (CSV) format.
- Generate plots of trial data.
- Analytical functions and views can be easily extended based on its Model-View-Controller architecture

## Prerequisites
Inflam requires the following Python packages:

- [NumPy](https://www.numpy.org/) - makes use of NumPy's statistical functions.
- [Matplotlib](https://matplotlib.org/stable/index.html) - uses Matplotlib to generate statistical plots

The following optional packages are required to run Inflam's unit tests:

- [pytest](https://docs.pytest.org/stable/) - Inflam's unit tests are written using pytest
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit testing

## Installation
Can be installed and run by cloning this git repository and running the below commands:

```bash
git clone git@github.com:JBello1610/python-intermediate-inflammation.git
cd python-intermediate-inflammation/
python inflammation-analysis.py
```
