for file in *_R[12]_001.fastq.gz; do
  new_name="${file/_R1_001.fastq.gz/_R1.fastq.gz}"
  new_name="${new_name/_R2_001.fastq.gz/_R2.fastq.gz}"
  mv "$file" "$new_name"
done

for file in *_R1.fastq.gz; do
  prefix="${file%_R1.fastq.gz}"
  mkdir -p "$prefix/raw_data/"
  mv "${prefix}_R1.fastq.gz" "$prefix/raw_data/"
  mv "${prefix}_R2.fastq.gz" "$prefix/raw_data/"
done
