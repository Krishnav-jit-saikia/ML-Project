from setuptools import find_packages , setup
from typing import List

def get_requirements(file_path : str) ->List[str]:  # This code means get_requirements is a function that will take the file_path which is in the string(str) format and it will return thr output in the form of List  of the strings
    '''
    This function will  return the list of requirements'''

    requirements = []
    with open(file_path) as file_obj :
        requirements= file_obj.readlines()
        requirements=[req.replace('\n', "")for req in requirements]

    return requirements





setup(
    name = "ML Project",
    version="0.0.1",
    author="Krishnav jit saikia",
    author_email="krishnavsaikia14@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)