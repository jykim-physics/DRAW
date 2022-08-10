#!/bin/bash
from os import path
from yaml import safe_load

from DRAW import __file__ as package_init_path

def read_yaml_to_dict(cfg_name):

    cfg_path = path.dirname(package_init_path) + f"/configs/{cfg_name}.yaml"
    with open(cfg_path, "r") as file:
        cfg = safe_load(file)

    return cfg

print(read_yaml_to_dict(vegetables))
