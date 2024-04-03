# googlesearch
googlesearch is a Python library for searching Google, easily. googlesearch uses requests and BeautifulSoup4 to scrape Google. 

## Installation
To install, run the following command:
```bash
python3 -m pip install googlesearch-python
```

## Usage
To get results for a search term, simply use the search function in googlesearch. For example, to get results for "Google" in Google, just run the following program:
```python
from googlesearch import search
search("Google")
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

### Time-Based Search (tbs) Parameter
You can also refine search results based on time. The tbs parameter allows you to filter results by various time ranges. For instance, to get results from the past hour, use `qdr:h`, or for results from the past year, use `qdr:y`. Here's how you can use the tbs parameter:
```python
from googlesearch import search
search("Google", tbs="qdr:h")  # Results from the past hour
search("Google", tbs="qdr:m")  # Results from the past month
search("Google", tbs="qdr:y")  # Results from the past year
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
