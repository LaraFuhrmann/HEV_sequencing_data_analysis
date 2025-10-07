import pandas as pd
import re
import pysam
import yaml

def yaml_to_dataframe(filepath):
    with open(filepath, 'r') as file:
        yaml_data = yaml.safe_load(file)

    rows = []
    for sample_name, values in yaml_data.items():
        row = {'sample_name': sample_name}
        row.update(values)
        rows.append(row)

    df = pd.DataFrame(rows)
    return df

def count_mapped_unmapped_reads(bam_file_path):
    with pysam.AlignmentFile(bam_file_path, "rb") as bam_file:
        total_reads = bam_file.count(until_eof=True)
        mapped_reads = bam_file.count()  # Default counts mapped reads only
        unmapped_reads = total_reads - mapped_reads
    return mapped_reads, unmapped_reads


def main(fnames, bams, fname_out):
    tmp = []
    for fname, bam in zip(fnames, bams):
        df = yaml_to_dataframe(fname)
        mapped, unmapped = count_mapped_unmapped_reads(bam)
        df['mapped'] = mapped
        df['unmapped'] = unmapped

    pd.concat(tmp).to_csv(fname_out)

if __name__ == "__main__":
    main(
        snakemake.input.fnames,
        snakemake.input.bams,
        snakemake.output.fname,
    )
