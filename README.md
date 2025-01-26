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
If you want to have unique links in your search result, you can use the `unique` option as in the following program.
```python
from googlesearch import search
search("Google", num_results=100, unique=True)
```
In addition, you can change the language google searches in. For example, to get results in French run the following program:
```python
from googlesearch import search
search("Google", lang="fr")
```
You can also specify the region ([Country Codes](https://developers.google.com/custom-search/docs/json_api_reference#countryCodes)) for your search results. For example, to get results specifically from the US run the following program:
```python
from googlesearch import search
search("Google", region="us")
```
If you want to turn off the safe search function (this function is on by default), you can do this:
```python
from googlesearch import search
search("Google", safe=None)
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

```
If requesting more than 10 results, but want to manage the batching yourself? 
Use `start_num` to specify the start number of the results you want to get:
```python
from googlesearch import search
search("Google", sleep_interval=5, num_results=200, start_result=10)
```

If you are using a HTTP Rotating Proxy which requires you to install their CA Certificate, you can simply add `ssl_verify=False` in the `search()` method to avoid SSL Verification.
```python
from googlesearch import search

proxy = 'http://API:@proxy.host.com:8080/'

j = search("proxy test", num_results=100, lang="en", proxy=proxy, ssl_verify=False)
for i in j:
    print(i)
```

Asyncio implementations disabled the `ssl_verify` key, which is seemingly not accepted by httpx.
A simple example:
```python
import asyncio
from googlesearch import search

async def main():
    proxy='http://API:@proxy.host.com:8080'
    r = search("hello world", advanced=True, proxy=proxy)
    async for i in r:
        print(i)

r = asyncio.run(main())
```