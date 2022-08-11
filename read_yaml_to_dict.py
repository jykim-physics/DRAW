#!/bin/bash
import os
from os import path
from yaml import safe_load

#from DRAW import __file__ as package_init_path


package_init_path = __file__
print(__file__)
print(path.dirname(package_init_path))
#package_init_path = os.path.dirname(__file__)

def read_yaml_to_dict(cfg_name):

    cfg_path = path.dirname(package_init_path) + f"/configs/{cfg_name}.yaml"
    with open(cfg_path, "rb") as file:
        cfg = safe_load(file)

    return cfg

print(read_yaml_to_dict("vegetables"))
