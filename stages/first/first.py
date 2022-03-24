import os
import shutil

from .get_antigen_chain import get_antigen_chain
from .repair_pdb_to_complex import repair_pdb_to_complex
from .change_chains_antibodies import change_chains_antibodies


def first(antibody, antigen, antigen_pdb, antigen_chain):
    antibody_HC_path = os.path.join(
        os.getcwd(), "antibodies", f"{antibody}_HC.pdb")
    antibody_LC_path = os.path.join(
        os.getcwd(), "antibodies", f"{antibody}_LC.pdb")

    if not ((os.path.isfile(antibody_HC_path)) and (os.path.isfile(antibody_LC_path))):
        return False

    antigen_pdb_path = os.path.join(os.getcwd(), "antigens", antigen_pdb)
    if not os.path.isfile(antigen_pdb_path):
        return False

    antigen_split = antigen.split(":")
    if len(antigen_split) == 3:
        complex_folder = os.path.join(
            os.getcwd(), "results", f"{antibody}-{antigen_split[2]}")
        os.mkdir(complex_folder)

    shutil.copyfile(antibody_HC_path, os.path.join(
        complex_folder, f"{antibody}_HC.pdb"))
    shutil.copyfile(antibody_LC_path, os.path.join(
        complex_folder, f"{antibody}_LC.pdb"))
    shutil.copyfile(antigen_pdb_path, os.path.join(
        complex_folder, f"{antigen_pdb}"))

    result = get_antigen_chain(
        antigen_pdb=antigen_pdb, antigen_chain=antigen_chain, complex_folder=complex_folder)

    if result == False:
        return False
    
    row = [complex_folder, antigen_pdb, antigen_chain, "A",
           f"{antibody}_HC.pdb", "A", "H", f"{antibody}_LC.pdb", "A", "L"]

    result = repair_pdb_to_complex(row=row)

    if result == False:
        return False
    
    result = change_chains_antibodies(row=row)

    if result == False:
        return False

    return True
