import os, sys

def addModulePath(file):
    utils_path = os.path.dirname(os.path.abspath(file)) + "/../utils"
    sys.path.append(utils_path)

