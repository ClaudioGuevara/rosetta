import os
import shutil
import random

import pandas as pd

from stages.first.first import first


def main():
    # Creamos la carpeta donde almacenaremos los complejos.
    results_directory = os.path.join(os.getcwd(), './results')

    if os.path.isdir(results_directory):
        shutil.rmtree(results_directory)
        os.mkdir(results_directory)
    else:
        os.mkdir(results_directory)        

    # Leemos el datasets que resumen todas las interacciones antígeno-anticuerpo.
    df = pd.read_csv(os.path.join(
        os.getcwd(), "./datasets/antigen_antibody_interactions.csv"))

    for i in range(1000):
        result = first(antibody=df["antibody"].iloc[i], antigen=df["antigen"].iloc[i],
                       antigen_pdb=df["antigen_pdb"].iloc[i], antigen_chain=df["chain"].iloc[i])

        if result == False:
            continue

if __name__ == "__main__":
    main()
