import os
from pathlib import Path
import logging

## CURRENT Time with message
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "cnnClassifier"

#.github - All CICD Related commands will be written in this file 


list_of_files = [
    ".github/workflows/.gitkeep",
    ##  Creating the constructor file unders local package folder
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]

## Common File paths related issue are resolved using Path 
for filepath in list_of_files:
    filepath = Path(filepath)

    ## It returns folder and file path 
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        ## If filedir val is available we will create the dir
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    ## Creating the empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")