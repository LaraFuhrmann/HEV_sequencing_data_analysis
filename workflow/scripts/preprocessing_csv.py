import pandas as pd
import re

def parse_stats_file_with_path(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    data = {}
    pattern = re.compile(r'^(.*?):\s+([\d,\.]+)(?:\s*\([^)]*\))?$')
    for line in lines:
        line = line.strip()
        match = pattern.match(line)
        if match:
            key = match.group(1)
            val = match.group(2).replace(',', '')
            if '.' in val:
                val = float(val)
            else:
                val = int(val)
            data[key] = val
    data['filepath'] = filepath
    df = pd.DataFrame([data])
    return df


def main(fnames, fname_out):
    tmp = []
    for fname in fnames:
        tmp.append(
            parse_stats_file_with_path(fname)
        )
    pd.concat(tmp).to_csv(fname_out)

if __name__ == "__main__":
    main(
        snakemake.input.fnames,
        snakemake.output.fname,
    )
