# Population density and education level correlation

[![Build Status](https://travis-ci.org/rr39943/pop_density-edu_level.svg?branch=master)](https://travis-ci.org/rr39943/pop_density-edu_level)
[![codebeat badge](https://codebeat.co/badges/045ca497-dbff-4a7d-a45e-61569840ca5b)](https://codebeat.co/projects/github-com-rr39943-pop_density-edu_level-master)

This repository is a test repository to analyse and test best practices in data management. It analyses data from Swiss cantons to determine if a correlation exists
between population density and percent of people that have a University or equivalent
diploma.

## Prerequisites
Standard version of python 3.6 with the libraries stated in [requirements.txt](./requirements.txt).

## Installation

Example of Linux installation with [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io):
```
mkvirtualenv demoData
workon demoData
git clone https://github.com/rr39943/pop_density-edu_level.git
pip install -r requirements.txt
```

## Usage
* Build processed data: run the Snakefile with command "snakemake"
* Clean the "intermidate_data" and "processed_data" with command "snakemake clean"
* Launch the tests with command "python -m unittest"

**Snakemake Rules:**

![rules](/documentation/rulegraph.png)

## Data description
* List of files: [files_description.md](documentation/files_description.md)
* Metadata: [codebook.md](./documentation/codebook.md)

## Authors
* **Raphaël Rey:** [raphael.rey@epfl.ch](mailto:raphael.rey@epfl.ch)

## License
This project is licensed under the MIT License - see the [LICENSE.md](./LICENSE.txt) file for details.
