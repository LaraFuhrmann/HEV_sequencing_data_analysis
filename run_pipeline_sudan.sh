#!/usr/bin/env bash
sbatch \
  --mail-type=END \
  --mem-per-cpu=2000 \
  --time=120:00:00 \
  -o snake_sudan.out -e snake_sudan.err \
snakemake \
--profile profile_simple/ \
-s workflow/Snakefile_sudan \
--rerun-incomplete \
--keep-incomplete \
-pr \
--cores 200 \
--use-conda \
--latency-wait 30 \
--show-failed-logs \
"$@"
