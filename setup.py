from setuptools import find_namespace_packages, setup

def get_requirements(file_path: str) -> list:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        # Remove '-e .' if it exists
        if "-e ." in requirements:
            requirements.remove("-e .")
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Sai Kishan',
    author_email='saikishan2452003@gmail.com',
    packages=find_namespace_packages(),
    install_requires=get_requirements('requirements.txt')
)
