
from setuptools import setup, find_packages

setup(
    name="fibonacci_service",         
    version="0.1.0",                 
    author="Perman ATAYEV",               
    author_email="bguuchin@gmail.com",     
    description="REST service for Fibonacci numbers and palindromes",
    packages=find_packages(where="src"),
    package_dir={"": "src"},          
    install_requires=[                
        "fastapi==0.95.1",
        "uvicorn==0.22.0",
        "pytest==7.3.1",
        "httpx==0.24.1"
    ],
    python_requires=">=3.8",          
    classifiers=[                     
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
