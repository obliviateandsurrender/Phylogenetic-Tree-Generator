# **Phylogenetic Tree Generator**

------

#### Introduction

This project consist of 4 scripts that are written to generate a phylogenetic relationship using UPGMA method for the series of data provided. This doesn't use bio-pyhton module and hence is a from the scratch aprroach for acheiving the said requirement.

A tabular representation is provided below.

#### Method Flow

| Script Name  | Input                                    | Ouput                         |
| ------------ | :--------------------------------------- | ----------------------------- |
| dnadm        | DNA sequence in Fasta format             | Distance Matrix in CSV format |
| dnaupgma     | Distance Matrix in CSV format            | Phylogenetic relation         |
| proteindm    | Protein sequence in Fasta format and BLOSUM matrix in CSV | Distance Matrix in CSV format |
| proteinupgma | Distance Matrix in CSV format            | Phylogenetic relation         |

By default the naming convention used are Ndistance and Pdistance for distance matrix produced and BLOSUM62 for the protien score card. You can change it to whatever you want.

#### Environment

It reuqires =python3= and is tested to be working on Windows and Linux (debian).