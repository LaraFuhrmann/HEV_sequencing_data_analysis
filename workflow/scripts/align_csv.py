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

def main(fnames, bams, fname_out):
    tmp = []
    for fname, bam in zip(fnames, bams):
        df = yaml_to_dataframe(fname)
        # reference sequence name, sequence length, # mapped read-segments and # unmapped read-segments
        idxstats = pysam.idxstats(bam).split("\t") # ex. 'PQ268485\t7135\t13001354\t0\n*\t0\t0\t0\n'
        df['reference_sequence_name'] = idxstats[0]
        df['sequence_length'] = idxstats[1]
        df['mapped_reads'] = idxstats[2]
        df['unmapped_reads'] = idxstats[3]
        tmp.append(df)

    pd.concat(tmp).to_csv(fname_out)

if __name__ == "__main__":
    main(
        snakemake.input.fnames,
        snakemake.input.bams,
        snakemake.output.fname,
    )
