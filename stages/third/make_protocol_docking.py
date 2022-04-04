import os

def make_protocol_docking(complex_folder):
    docking_protocol = os.path.join(complex_folder, "docking_full3.xml")
    docking_protocol = docking_protocol.replace("\n", "")
