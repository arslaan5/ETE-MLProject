from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'


def get_requirements(file_path:str)->List[str]:
    """Get the list of requirements from a file."""
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if (HYPHEN_E_DOT) in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements


setup(
    name='End-to-End Machine Learning Project',
    version='0.1',
    author='Arslaan Siddiqui',
    author_email='arslaansiddiqui365@gmail.com',
    description='This is an end-to-end guided machine learning project from Krish Naik youtube channel',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)