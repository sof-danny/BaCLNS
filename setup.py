from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='BaCLNS',  
    version='0.1.0', 
    description='Efficient Backstepping Control for Linear and Nonlinear Dynamic Systems',
    long_description=long_description,
    long_description_content_type='text/markdown',  
    url='https://github.com/sof-danny/BaCLNS', 
    author='Samuel O. Folorunsho',
    author_email='folorunshosamuel001@gmail.com',
    packages=find_packages(), 
    install_requires=[
        'numpy',
        'sympy',
        'matplotlib',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
