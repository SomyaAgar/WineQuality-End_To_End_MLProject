import setuptools

with open("README.md", "r", encoding ="utf-8") as f:
    long_description = f.read()

__version__ ="0.0.0"

REPO_NAME= "WineQuality-End_To_End_MLProject"
AUTHOR_USER_NAME = "SomyaAgar"
SRC_REPO ="mlProject"
AUTHOR_EMAIL ="somyaagar2001@gmail.com"

setuptools.setup(
    name= SRC_REPO,
    version =__version__,
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= "Python package for ML app",
    long_description= long_description,
    long_description_content = "text/markdown",
    url =f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls ={
        "BugTracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where= 'src')
)