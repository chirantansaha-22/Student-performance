from setuptools import find_packages, setup

REQUIREMENT_FILE_NAME='requirements.txt'
HYPHEN_E_DOT ='-e .'

def get_requirements(filename:str):
    requirements = []

    with open(filename,'r') as f:
        requirements = f.readlines()
        requirements = [requirement.replace("\n","") for requirement in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements


setup(
    name="student-performance",
    version="0.0.1",
    author="Chirantan Saha",
    author_email="projects.cs22@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(REQUIREMENT_FILE_NAME)
)