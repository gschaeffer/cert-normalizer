from setuptools import setup

# https://python-packaging.readthedocs.io/en/latest/index.html

with open("README.md", "r") as f:
    description = f.read()

setup(
    author="G Schaeffer",
    author_email="gschaeffer@gmail.com",
    description="Normalize raw data.",
    include_package_data=True,
    install_requires=[
        "arrow",
        "flask",
        "google-cloud-firestore",
        "spacy",
    ],
    license="MIT",
    long_description=description,
    long_description_content_type="text/markdown",
    name="normalizer",
    packages=["normalizer"],
    python_requires=">=3.9",
    url="http://github.com/gschaeffer/cert-normalizer",
    version="0.0.1",
    zip_safe=False,
)
