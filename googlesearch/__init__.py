"""googlesearch is a Python library for searching Google, easily."""
import gzip
import re
import zlib
from time import sleep
from urllib.parse import quote_plus

import brotli
import requests
from bs4 import BeautifulSoup
from requests import get
from .user_agents import _get_useragent, get_random_header

def _req_post(term, results=10, lang="en", proxies=None, timeout=10):

    """
    Sends a request to Google Search and returns the response.

    Attributes:
        term (str): The term to search for.
        results (int): The number of results to return.
        lang (str): The language to search in.
        proxies (dict): A dictionary of proxies to use.
        timeout (int): The timeout for the request.

    """
    # Get random header
    header = get_random_header()

    data = {
        'bl': 'boq_identityfrontenduiserver_20230625.09_p0',
        'x': '8',
        'gl': 'GB',
        'm': '0',
        'app': '0',
        'pc': 'srp',
        'continue': f'https://www.google.com/search?q={term}&hl={lang}&num={results}&start=0&gbv=1&sei=qrCcZOfUH5DskdUPib21oA4',
        'hl': 'en',
        'uxe': 'none',
        'set_eom': 'false',
        'set_sc': 'true',
        'set_aps': 'true',
    }
    response = requests.post('https://consent.google.com/save', data=data, headers=header, proxies=proxies, timeout=timeout)
    response.raise_for_status()

    return response


def _req(term, results, lang, start, proxies, timeout):
    resp = get(
        url="https://www.google.com/search",
        headers={
            "User-Agent": _get_useragent()
        },
        params={
            "q": term,
            "num": results + 2,  # Prevents multiple requests
            "hl": lang,
            "start": start,
        },
        proxies=proxies,
        timeout=timeout,
    )
    resp.raise_for_status()
    return resp


class SearchResult:
    def __init__(self, url, title, description):
        self.url = url
        self.title = title
        self.description = description

    def __repr__(self):
        return f"SearchResult(url={self.url}, title={self.title}, description={self.description})"

def decode_content(response):

    content = None

    try:
        content = response.content
        encoding = response.headers.get('content-encoding', '').lower()
        charsets = response.headers.get('content-type', '').lower()

        # Apply decoding for multiple content codings
        for coding in reversed(encoding.split(',')):
            if coding.strip() == 'gzip':
                content = gzip.decompress(content)
            elif coding.strip() == 'deflate':
                content = zlib.decompress(content)
            elif coding.strip() == 'compress':
                content = zlib.decompress(content, -zlib.MAX_WBITS)
            elif coding.strip() == 'br':
                content = brotli.decompress(content)
            else:
                pass  # unknown coding, ignore it

        # Determine the charset
        for charset in charsets.split(';'):
            if charset.strip().startswith('charset='):
                return content.decode(charset.split('=')[1])
        return content.decode('utf-8')  # fallback to utf-8

    except Exception as e:
        return content.decode("utf-8")

def search_post(term, num_results=10, lang="en", sleep_interval=0, proxies=None, timeout=10, attempts=5):
    """
    Search the Google search engine, but bypass the JS issue by posting the request instead of get.
    Returns a list of urls.

    Attributes:
        term (str): The term to search for.
        num_results (int): The number of results to return.
        lang (str): The language to search for.
        sleep_interval (int): The time to sleep between requests.
        proxies (dict): A dictionary of proxies to use.

        attempts (int): The number of attempts to make before giving up.

    """

    escaped_term = quote_plus(term) # make 'site:xxx.xxx.xxx ' works.

    # Proxy

    # Fetch
    tries = 0
    while tries < attempts:

        # Post and get response
        resp = _req_post(escaped_term, num_results, lang, proxies, timeout)
        # Decode content if needed
        decoded_content = decode_content(resp)
        # use regex to find all urls
        results = re.findall(r"/url\?q=([^&]+)", decoded_content)

        if len(results) > 0:
            return results

        sleep(sleep_interval)
        tries += 1

    return []

def search(term, num_results=10, lang="en", proxy=None, advanced=False, sleep_interval=0, timeout=5, post=False):
    """Search the Google search engine"""

    escaped_term = quote_plus(term) # make 'site:xxx.xxx.xxx ' works.

    # Proxy
    proxies = None
    if proxy:
        if proxy.startswith("https"):
            proxies = {"https": proxy}
        else:
            proxies = {"http": proxy}

    # Fetch
    start = 0
    while start < num_results:
        # Send request
        if post:
            resp = _req_post(escaped_term, num_results - start, lang, start, proxies, timeout)
        else:
            resp = _req(escaped_term, num_results - start, lang, start, proxies, timeout)

        # Parse
        soup = BeautifulSoup(resp.text, "html.parser")
        result_block = soup.find_all("div", attrs={"class": "g"})
        if len(result_block) ==0:
            start += 1
        for result in result_block:
            # Find link, title, description
            link = result.find("a", href=True)
            title = result.find("h3")
            description_box = result.find(
                "div", {"style": "-webkit-line-clamp:2"})
            if description_box:
                description = description_box.text
                if link and title and description:
                    start += 1
                    if advanced:
                        yield SearchResult(link["href"], title.text, description)
                    else:
                        yield link["href"]
        sleep(sleep_interval)

        if start == 0:
            return []
