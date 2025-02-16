'''
Kendra Vilfort
1/5/2025
HackBio Biocoding Internship
Stage One Task
'''


print("Part 1\n")

def dna_to_protein(dna_sequence):
    final_dna_sequence = dna_sequence.upper()
    dna_to_rna_complement = {
        'A': 'U',  # Adenine -> Uracil
        'T': 'A',  # Thymine -> Adenine
        'C': 'G',  # Cytosine -> Guanine
        'G': 'C'  # Guanine -> Cytosine
    }

    rna_sequence = ''.join(dna_to_rna_complement[base] for base in final_dna_sequence)
    print("Complentary RNA sequence:", rna_sequence)


    codons= [rna_sequence[i:i+3] for i in range(0, len(rna_sequence), 3)]
    print ("Codons:",codons)

    codon_to_amino_acid = {
        'AUG': 'M',  # Start codon (Methionine)
        'UUU': 'F', 'UUC': 'F',  # Phenylalanine
        'UUA': 'L', 'UUG': 'L',  # Leucine
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',  # Leucine
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I',  # Isoleucine
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',  # Valine
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',  # Serine
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',  # Proline
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',  # Threonine
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',  # Alanine
        'UAU': 'Y', 'UAC': 'Y',  # Tyrosine
        'CAU': 'H', 'CAC': 'H',  # Histidine
        'CAA': 'Q', 'CAG': 'Q',  # Glutamine
        'AAU': 'N', 'AAC': 'N',  # Asparagine
        'AAA': 'K', 'AAG': 'K',  # Lysine
        'GAU': 'D', 'GAC': 'D',  # Aspartic Acid
        'GAA': 'E', 'GAG': 'E',  # Glutamic Acid
        'UGU': 'C', 'UGC': 'C',  # Cysteine
        'UGG': 'W',  # Tryptophan
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',  # Arginine
        'AGU': 'S', 'AGC': 'S',  # Serine
        'AGA': 'R', 'AGG': 'R',  # Arginine
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',  # Glycine
        'UAA': '*STOP*', 'UAG': '*STOP*', 'UGA': '*STOP*'  # Stop codons
    }

    protein_sequence = ''
    for codon in codons:
        amino_acid = codon_to_amino_acid.get(codon)  # Get amino acid or empty string if codon is invalid
        protein_sequence += amino_acid
        if amino_acid == '*STOP*':  # Stop translation at stop codon
            break


    print("Protein Sequence:",protein_sequence)
    return protein_sequence

dna_to_protein("atacggtac")

print("--------------------------------------------------------------------------------------\n")
print("Part 2\n")

def logistic_growth(initial_population, max_population, growth_rate, time, t_lag):
    population = initial_population
    for hour in range(time):
        population = max_population / (1 + (2.71828 ** (-growth_rate*(hour - t_lag))))

    return population

growth_curves = {}
for i in range(1, 101):

    initial_population = i * 10
    max_population = 1000 + i * 5
    growth_rate = 0.1 + (i * 0.01)
    time = 100
    t_lag = i

    curve_name = f"Curve_{i}"
    final_population = logistic_growth(initial_population, max_population, growth_rate, time, t_lag)
    growth_curves[curve_name] = final_population

for curve, population in growth_curves.items():
    print(f"{curve}: Final Population = {population:.2f}")

print("--------------------------------------------------------------------------------------\n")
print("Part 3\n")

import math

def time_to_reach_80_percent(max_population, growth_rate, t_lag):
    target_population = 0.8 * max_population

    time_to_80 = t_lag + math.log((max_population / target_population) - 1) / -growth_rate

    print(f"It takes {time_to_80:.2f} hours to reach 80% of maximum growth.")
    return time_to_80

time_to_reach_80_percent(100,1.5,10)

print("--------------------------------------------------------------------------------------\n")
print("Part 4\n")

def hamming_distance(slack_username, twitter_handle):
    if len(slack_username) != len(twitter_handle):
        raise ValueError("The Slack username and Twitter handle must be of the same length.")
    distance = 0

    for i in range(len(slack_username)):
        if slack_username[i] != twitter_handle[i]:
            distance += 1
    print(f"The Hamming distance is: {distance}")
    return distance

hamming_distance("usern4m3", "username")