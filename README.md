# Population density and education level correlation

This repository analyse data from Swiss cantons to determine if a correlation exists
between population density and percent of people that have a University or equivalent
diploma.

## Prerequisites
* Standard version of python 3.6 with the libraries stated in [requirements.txt](./requirements.txt).
* Matplotlib (install with "sudo apt-get install python3-matplotlib" on Linux)

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
This project is licensed under the MIT License - see the [LICENSE.md](./LICENSE.md) file for details.
