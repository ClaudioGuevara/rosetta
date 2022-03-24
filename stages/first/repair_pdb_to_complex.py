import os

from pdbfixer import PDBFixer
from simtk.openmm.app import PDBFile


def repair_pdb_to_complex(complex_folder, antigen_pdb, antigen_chain, antibody):
    try:
        row = [complex_folder, antigen_pdb, antigen_chain, "A",
           f"{antibody}_HC.pdb", "A", "H", f"{antibody}_LC.pdb", "A", "L"]

        antigen_data = row[1:4]
        antibody_HC_data = row[4:7]
        antibody_LC_data = row[7:11]

        new_row = [antigen_data, antibody_HC_data, antibody_LC_data]

        for element in new_row:
            fixer = PDBFixer(filename=os.path.join(complex_folder, element[0]))
            filename = element[0].replace(".pdb", "")
            fixer.findMissingResidues()
            fixer.findNonstandardResidues()
            fixer.replaceNonstandardResidues()
            fixer.removeHeterogens(True)
            fixer.findMissingAtoms()
            fixer.addMissingAtoms()
            fixer.addMissingHydrogens(7.0)
            PDBFile.writeFile(fixer.topology, fixer.positions, open(
                os.path.join(complex_folder, f"{filename}_repaired.pdb"), "w"))

            return True
    except:
        return False
