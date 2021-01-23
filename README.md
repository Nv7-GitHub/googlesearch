# googlesearch
googlesearch is a Python library for searching Google, easily. googlesearch uses requests and BeautifulSoup4 to scrape Google. 

## Installation
To install, run the following command:
```bash
python3 -m pip install googlesearch-python
```

## usage
To get results for a search term, simply use the search function in googlesearch. For example, to get results for "Google" in Google, just run the following program:
```python
from googlesearch import search
search("Google")
```

## Additional options
googlesearch supports a few additional options. By default, googlesearch returns 10 results. This can be changed. To get a 100 results on Google for example, run the following program.
```python
from googlesearch import search
search("Google", results_per_page=100)
```

googlesearch also supports pagination. By default, num_results is -1. That will return all available pages.

In this example, num_results=200. That will return results in each page until 200 results are reached, or no more pages are found.
```python
from googlesearch import search
search("Google", results_per_page=100, num_results=200)
```
In addition, you can change the language google searches in. For example, to get results in French run the following program:
```python
from googlesearch import search
search("Google", lang="fr")
```
## googlesearch.search
```python
googlesearch.search(str: term, int: num_results=10, str: lang="en") -> list
```
