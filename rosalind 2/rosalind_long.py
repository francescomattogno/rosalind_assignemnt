def read_fasta(fasta):
    sequences = []
    fasta_sequences = fasta.strip().split('>')
    for seq in fasta_sequences:
        lines = seq.split('\n')
        header = lines[0]
        seq = ''.join(lines[1:])
        if header.startswith("Rosalind_"):
            sequences.append(seq)
    return sequences

def overlap(x, y):
    
    for i in range(1, len(x)):
        if y.startswith(x[i:]):
            max_overlap = len(x) - i
            break
    return max_overlap

def shortstring(seqs):
    while len(seqs) > 1:
        max_overlap_len = -1
        best_1, best_2 = -1, -1

        for seq1 in range(len(seqs)):
            for seq2 in range(len(seqs)):
                if seq1 != seq2:
                    overlap_len = overlap(seqs[seq1], seqs[seq2])
                    if overlap_len > max_overlap_len:
                        max_overlap_len = overlap_len
                        best_1, best_2 = seq1, seq2

        if best_1 != -1 and best_2 != -1:
            merged_string = sequences[best_1] + sequences[best_2][max_overlap_len:]
            sequences.pop(best_1)
            sequences.pop(best_2 - 1 if best_2 > best_1 else best_2)
            sequences.append(merged_string)

    return sequences[0]

input_data = """copy input file here"""

sequences = read_fasta(input_data)
shortest_superstring = shortstring(sequences)
print(shortest_superstring)