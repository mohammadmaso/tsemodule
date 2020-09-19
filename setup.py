# replace:
# <your_package> with your actual package name.
# <you> with your name.
# <your_email> with your public email address.
# <your_github_repo_url> with your github project's url.
from setuptools import setup, find_packages

s = setup(
    name="tsemodule",
    version="1.0.0",
    license="MIT",
    description="",
    url='<your_github_repo_url>",
    packages=find_packages(),
    install_requires=[],
    python_requires = ">= 3.4",
    author="<you>",
    author_email="<your_email>",
    )