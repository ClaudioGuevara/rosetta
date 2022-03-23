import os
import shutil

import pandas as pd

from pymol import cmd


def get_chain_antigen():
    antigens_directory = "./antigens"
    antigen_pdb = "Q9BYR6.pdb"

    cmd.load(os.path.join(antigens_directory, antigen_pdb))
    pdb_code = antigen_pdb.replace(".ent", "").replace(".pdb", "")
    cmd.select("chainAntigen", str(pdb_code)+" and chain A")
    cmd.alter(("chain A"), "chain = 'A'")
    cmd.indicate("hetatm")
    cmd.remove("indicate")
    cmd.save(antigens_directory+"/"+pdb_code +
             "_A.pdb", "chainAntigen", -1, "pdb")


def make_folder_and_copy_structures():
    antibodies_directory = "./antibodies"
    interacting_antibody = "A021"
    interacting_antigen = "Hs~Ref:NM_033185.2~uORF:IOH40389"
    path_complexes= "./results"

    row = []

    if ((os.path.isfile(f"{antibodies_directory}/{interacting_antibody}_HC.pdb")) and (os.path.isfile(f"{antibodies_directory}/{interacting_antibody}_LC.pdb"))):
        
        df = pd.read_csv("./resume_antigen_info.csv")
        antigen_data = df[df["Id_antigen"] == interacting_antigen].values.tolist()
        
        if len(antigen_data) == 1:
            name_dir_complex= interacting_antibody+"-"+antigen_data[0][0].split(":")[-1]
            name_file=antigen_data[0][2].replace(".ent", "").replace(".pdb","")+"_A.pdb"
            print(antigen_data[0][3])
            if os.path.isfile(os.path.join("./results", name_dir_complex)):
                shutil.rmtree(os.path.join("./results", name_dir_complex))
                os.mkdir(os.path.join("./results", name_dir_complex))

            shutil.copyfile(f"{antibodies_directory}/{interacting_antibody}_HC.pdb", f"./results/{name_dir_complex}/{interacting_antibody}_HC.pdb")
            shutil.copyfile(f"{antibodies_directory}/{interacting_antibody}_HC.pdb", f"./results/{name_dir_complex}/{interacting_antibody}_LC.pdb")
            shutil.copyfile(f"./antigens/{name_file}", f"./results/{name_dir_complex}/{name_file}")

            return row
        else:
            return row

    else:
        return row


def main():
    get_chain_antigen()
    
    row_info = make_folder_and_copy_structures()
    if len(row_info) == 0:
        return


if __name__ == "__main__":
    main()
