#The setup.py file is used when you're packaging your Python project so others can install it easily — like how you install libraries using pip.
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)-> list[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements
setup(
    name='ML_Project',
    version='0.0.1',
    author='Vedant K.',
    author_email='vedantkolhapure111@gmail.com',
    packages=find_packages(),           # considers the src as a package
    install_requires = get_requirements('requirements.txt'),  
)