from setuptools import setup, find_packages

def split_paragraphs(path):
    first = ""
    rest = ""
    is_first = True
    with open(path) as f:
        for line in f:
            if len(line.strip()) == 0:
                is_first = False
            if is_first:
                first += line
            else:
                rest += line
    return (first.strip(), rest.strip())

(description, long_description) = split_paragraphs("README.rst")

setup(
    name="humblewx",
    version="0.2.0",
    description=description,
    long_description=long_description,
    url="https://github.com/thetimelineproj/humblewx",
    maintainer="Rickard Lindberg",
    maintainer_email="ricli85@gmail.com",
    license="GPLv3",
    packages=["humblewx"],
    package_dir={"": "source"},
)
