from setuptools import find_packages,setup
from typing import List


def get_requiremenets()-> List[str]:
    """
    this function return list of requirements
    """
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            #for each lines
            for line in lines:
                requirement=line.strip()
                #ignore empty lines and -e
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt not found ")
    return requirement_list
setup(
        name='NetworkSecurity',
        version="0.0.1",
        author='Mohd Faizy',
        author_email="faizyzaidi80@gmail.com",
        packages=find_packages(),
        install_requires=get_requiremenets()
    )
