from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."
## Function will return  a list 
def get_requirements(file_path:str) -> List[str]:
    '''
    It returns list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        ## Replacing \n with ''
        [req.replace("\n","") for req in requirements]
        ## -e . -- To install your current package . But in requirements -e . will also come
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name = 'mlproject',
    version='0.0.1',
    author='Lucky Rathod',
    author_email='luckyrathod46@gmail.com',
    ##  How it will identify that how many packages are there.
    ## Create a new src folder . Now if you want this src to be referred as package . Create __init.py__ inside folder
    packages= find_packages(),
    ## Project might contain hundreds of packaage 
    install_requires = get_requirements('requirements.txt')
)