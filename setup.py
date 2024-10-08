from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
setup(
    name='End-to-end-Image-Classification',
    version='0.0.1',
    author='Maaz Ahmad',
    author_email='maazahmad2404@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
    
)
