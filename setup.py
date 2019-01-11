import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="locadora-cin",
    version="0.0.1",
    author="Rennan Francisco Messias de Lima",
    author_email="mrennan.lima@gmail.com",
    description="Sistema para uma locadora",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rennanflima/locadora-cin",
    packages=setuptools.find_packages(),
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 2 - Pre-Alpha"
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: Portuguese (Brazilian)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Framework :: Django",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
    ],
)