# googlesearch
googlesearch is a Python library for searching Google, easily. googlesearch uses requests and BeautifulSoup4 to scrape Google. 

## Installation
To install, run the following command:
```bash
python3 -m pip install googlesearch-python
```

## Usage via GET
To get results for a search term, simply use the search function in googlesearch. For example, to get results for "Google" in Google, just run the following program:
```python
from googlesearch import search
search("Google")
```
## Usage via POST
To get results for a search term you can also user the POST method, which i've found can have better results, and is more reliable. For example, to get results for "Google" in Google, just run the following program:
Currently only basic functionality. See docstring for more.
```python
from googlesearch import search_post
search_post("Google")

```
## Additional options
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
To extract more information, such as the description or the result URL, use an advanced search:
```python
from googlesearch import search
search("Google", advanced=True)
# Returns a list of SearchResult
# Properties:
# - title
# - url
# - description
```
If requesting more than 100 results, googlesearch will send multiple requests to go through the pages. To increase the time between these requests, use `sleep_interval`:
```python
from googlesearch import search
search("Google", sleep_interval=5, num_results=200)
```