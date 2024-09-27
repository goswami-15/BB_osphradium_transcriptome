import sys
from Bio import AlignIO

def convert_fasta_to_phy(input_file, output_file):
    try:
        # Load the alignment from a FASTA file
        alignment = AlignIO.read(input_file, "fasta")
        # Write the alignment to a Phylip format (relaxed)
        AlignIO.write(alignment, output_file, "phylip-relaxed")
        print(f"Successfully converted {input_file} to {output_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_fasta_to_phy.py input.fasta output.phy")
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
        convert_fasta_to_phy(input_path, output_path)

