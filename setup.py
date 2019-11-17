import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ProctorExam-api-wrapper",
    version="0.0.1",
    author="Guillaume Baelen",
    author_email="guillaume.baelen@gmail.com",
    description="A wrapper for the ProctorExam’s API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gbaelen/ProctorExam-python-api-wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
