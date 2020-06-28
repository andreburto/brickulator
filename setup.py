import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="brickulator", # Replace with your own username
    version="0.0.2",
    author="Andy Burton",
    author_email="tuglyraisin-NOPE-@gmail.com",
    description="A library for calculating bricks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andreburto/brickulator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7.0',
)