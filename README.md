# googlesearch

googlesearch is a Python library for searching Google, easily. googlesearch uses requests and BeautifulSoup4 to scrape Google.

## Installation

To install, run the following command:

```sh
pip install googlesearch-python
```

## Usage

To get results for a search term, simply use the search function in googlesearch. For example, to get results for "Google" in Google, just run the following program:

```python
from googlesearch import search

search("Google")
```

### Advanced Usage

googlesearch supports a few additional options. By default, googlesearch returns 10 results. This can be changed. To get a 100 results on Google for example, run the following program.

```python
from googlesearch import search

search("Google", num_results=100)
```

In addition, you can change the language google searches in. For example, to get results in French run the following program:

```python
from googlesearch import search

search("Google", lang="fr")
```

## googlesearch.search

```python
googlesearch.search(term: str, num_results: int=10, lang: str="en") -> list
```

## Developer Documentation

### Prerequisites

- [Python 3.6+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/)

Install dependencies:

```sh
poetry install
```

Build the package:

```sh
poetry build
```

Publish the package:

```sh
poetry publish
```
