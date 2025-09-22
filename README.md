# Hepatitis E Virus Sequencing Data Analysis
This repository contains analysis scripts and resources for processing Illumina sequencing data of Hepatitis E virus (HEV) patient samples.

The analysis is conducted using two different reference sequences: one from Sudan and another from Uganda. The respective workflows are implemented as independent pipelines in `workflow/Snakefile_sudan` and `workflow/Snakemake_uganda`. Results from each workflow are organized separately in the directories `results_sudan` and `results_uganda`.

The configuration file `config/config.yaml` specifies the reference sequences used and the directories where the input data are located.
