from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="help_func", # the name that you will install via pip
    version="1.0",
    author="Carlos Knowles",
    author_email="cknowles4211@gmail.com",
    description="A package containing two helper functions to add a series to a dataframe and to split a column containing date time format data into separate columns for ML purposes.",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/Cknowles11/lambdata_cknowles11",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)