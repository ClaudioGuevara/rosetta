import os
import re

from utils.create_file import create_file
from .process_results_repack import process_results_repack
from .make_protocol_docking import make_protocol_docking

def main(complex_folder, antibody, antigen):
    result = process_results_repack(complex_folder=complex_folder, antibody=antibody, antigen=antigen)
    
    if result == False:
        return False
    
    # make_protocol_docking(complex_folder=complex_folder)

    

    