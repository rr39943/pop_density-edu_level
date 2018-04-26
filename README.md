# Population density and education level correlation

[![Build Status](https://travis-ci.org/rr39943/pop_density-edu_level.svg?branch=master)](https://travis-ci.org/rr39943/pop_density-edu_level)
[![codebeat badge](https://codebeat.co/badges/045ca497-dbff-4a7d-a45e-61569840ca5b)](https://codebeat.co/projects/github-com-rr39943-pop_density-edu_level-master)

This repository is a test repository to analyse and test best practices in data management. It analyses data from Swiss cantons to determine if a correlation exists
between population density and the share of population holding a university degree or equivalent.

## Prerequisites
* Standard version of python 3.6
* Python libraries listed in [requirements.txt](./requirements.txt).

## Installation

Example of Linux installation with [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io):
```
mkvirtualenv demoData
workon demoData
git clone https://github.com/rr39943/pop_density-edu_level.git
pip install -r requirements.txt
```

## Usage
* To build processed data, run the Snakefile with command "snakemake"
* To clean the "intermidate_data" and "processed_data", you may use command "snakemake clean"
* To launch the tests, use command "python -m unittest"

**Snakemake Rules:**

![rules](/documentation/rulegraph.png)

## Data description
* List of files: [files_description.md](documentation/files_description.md)
* Metadata: [codebook.md](./documentation/codebook.md)

## Authors
* **Raphaël Rey:** [raphael.rey@epfl.ch](mailto:raphael.rey@epfl.ch)

## License
This project is licensed under the MIT License - see the [LICENSE.md](./LICENSE.txt) file for details.
