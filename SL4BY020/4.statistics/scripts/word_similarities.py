#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
This script calculates the cosine similarities between 7 NGO discourses at COPs 25-26 for a specific keyword.

Example of use:

$ python word_similarities.py -k biodiversity

The NGOs are:
- EDF: Environment Defense Fund
- EJF: Environment Justice Foundation
- FoE: Friends of the Earth
- GP: Greenpeace
- NRDC: Natural Resources Defense Council
- OXFAM
- WWF: World Wide Fund for nature

About the Corpus:
> Pauline Bureau, Camille Biros, Caroline Peynaud, et al. (2024). Climate discourses [Corpus]. ORTOLANG (Open Resources and TOols for LANGuage) - www.ortolang.fr, v3.2, https://hdl.handle.net/11403/climate-discourses/v3.2.
"""

#
# Modules to import
#
import argparse
import numpy as np
import pandas as pd
import pickle

#
# User functions
#
def cosine_similarities(vectors):
    """Calculate the cosine similarities from vectors.

    data -- a list of vectors
    """
    x = np.zeros((len(vectors), len(vectors)))
    for i, row_i in enumerate(vectors):
        for j, row_j in enumerate(vectors):
            x[i, j] = np.dot(row_i, row_j) / np.dot(np.linalg.norm(row_i), np.linalg.norm(row_j))
    return x

def main(keyword):

    # load data frame
    with open('./word_embeddings.pickle', 'rb') as f:
        df = pickle.load(f)

    # an array of cosine similarities for the word 'action'
    results = cosine_similarities(df.loc[:, keyword].values)

    # put back the array into a dataframe
    data = pd.DataFrame(results, index=df.index, columns=df.index)

    print("-" * 40)
    print(f"Cosine similarities for word '{keyword}'")
    print("-" * 40)
    print(data)

#
# Main procedure
#
if __name__ == "__main__":

    # parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--keyword", type=str, required=True, help="Pick up a keyword among the list",
                        choices=['action', 'biodiversity', 'change', 'climate', 'community',
                                 'energy', 'group', 'impact', 'nature', 'support'])
    args = parser.parse_args()

    # launch the main procedure
    main(args.keyword)
