#!/usr/bin/env python

import argparse

#logging setup
console = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("Preprocess Peptides MHCNuggets")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)

def parse_mztab(identified_peptides_file):
       """
       parses an mztab file and returns all identified proteins

       :param identified_peptides_file: path to the mztab file
       :return: identified proteins
       """
       mztab = open(identified_peptides_file)
       mztab_read = mztab.readlines()
       mztab.close()

       seq_geneIDs = defaultdict(str)
       for line in mztab_read:
              if line.startswith("PEP"):
                     content = line.split('\t')
                     seq = content[1]
                     geneID = content[2]
                     if not 'U' in seq and not 'X' in seq and not 'Z' in seq and not 'J' in seq and not 'B' in seq:
                            seq_geneIDs[seq] = geneID

       return seq_geneIDs

def main():
    model = argparse.ArgumentParser(description='MHCNuggets binding prediction')

    model.add_argument(
        '-m', '--mztab',
        type=str,
        help='mztab file'
    )

    model.add_argument(
        '-o', '--output',
        type=str,
        help='preprocessed '
    )

    args = model.parse_args()

    seq_to_geneIDs = parse_mztab(args.mztab)

    # write just peptides new line formatted

    # write seq to geneID in a suitable format (csv?)

if __name__ == '__main__':
    main()