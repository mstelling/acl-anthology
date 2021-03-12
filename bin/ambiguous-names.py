#!/usr/bin/env python3

import yaml
import os

directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
ambig_names = []
with open("{}/data/yaml/name_variants.yaml".format(directory), "r") as f:
    names_dict = yaml.safe_load(f)
    # make a list of entries marked as ambiguous by the comment "May refer to several people"
    for i in names_dict:
        if "May refer to several people" in i.values():
            ambig_names.append(i)

# make a list of all the names marked as ambiguous
ambig_names_list = []
for i in ambig_names:
    ambig_names_list.append(i["canonical"])

# look for all instances of the ambiguous names, adding their ids to a new list inside the dict
for i in ambig_names_list:
    i_idlist = []
    for j in names_dict:
        if i == j["canonical"]:
            i_idlist.append(j["id"])
    i["ids"] = i_idlist

# at this point, ambig_names_list contains all of the ambiguous names and their IDs.

# Pretty printing:
print("The following names are shared:")
for i in ambig_names_list:
    print("{} {}, IDs: {}".format(i["first"],i["last"],i["ids"]))
    
