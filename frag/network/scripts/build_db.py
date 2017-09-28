import argparse
import os

from rdkit import Chem

from frag.network.models import NodeHolder,Edge,Attr
from frag.utils.network_utils import build_network, write_data

if __name__ == "__main__":

    # Read in a SD or SMILES file - then write out into a specified directory
    parser = argparse.ArgumentParser(description='Convert a SMILES or SDFile to input for Astex Fragment network.')
    parser.add_argument('--input')
    parser.add_argument('--base_dir')
    args = parser.parse_args()
    attrs = []
    id = 0
    for i,x in enumerate(Chem.SDMolSupplier(args.input)):
        attr = Attr(Chem.CanonSmiles(Chem.MolToSmiles(x)),["EM","EN"+str(i)])
        attrs.append(attr)
        id +=1
    if not os.path.isdir(args.base_dir):
        os.mkdir(args.base_dir)
    # Build the network
    node_holder = NodeHolder()
    node_holder = build_network(attrs,node_holder)
    # Write the data out
    write_data(args.base_dir,node_holder,attrs)