from setuptools import setup, find_packages

# Declaring variables for setup functions
PROJECT_NAME = "fipkart-review-scrapper"
VERSION = "0.0.1"
AUTHOR = "Ulkesh"
DESRCIPTION = "This project is to scrap flipkart website for product review"
REQUIREMENT_FILE_NAME = "requirements.txt"



setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESRCIPTION,
    packages=find_packages()
)
