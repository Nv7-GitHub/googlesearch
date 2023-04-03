from setuptools import setup

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

requirements=[
    "beautifulsoup4>=4.9",
    "requests>=2.20",
]

setup(
    name="googlesearch-python",
    version="1.2.1",
    author="Nishant Vikramaditya",
    author_email="junk4Nv7@gmail.com",
    description="A Python library for scraping the Google search engine.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nv7-GitHub/googlesearch",
    packages=["googlesearch"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[requirements],
)
