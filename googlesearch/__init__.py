"""googlesearch is a Python library for searching Google and Bing, easily."""
from time import sleep
from bs4 import BeautifulSoup
from requests import get
from .user_agents import get_useragent
import urllib


def _req(term, results, lang, start, proxies, timeout, engine):
    search_url = {
        "google": "https://www.google.com/search",
        "bing": "https://www.bing.com/search",
    }
    resp = get(
        url=search_url[engine],
        headers={
            "User-Agent": get_useragent()
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


def search(term, num_results=10, lang="en", proxy=None, advanced=False, sleep_interval=0, timeout=5, engine="google"):
    """Search the Google or Bing search engine"""

    escaped_term = urllib.parse.quote_plus(term) # make 'site:xxx.xxx.xxx ' works.

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
        resp = _req(escaped_term, num_results - start,
                    lang, start, proxies, timeout, engine)

        # Parse
        soup = BeautifulSoup(resp.text, "html.parser")
        if engine == "bing":
            result_block = soup.find_all("li", attrs={"class": "b_algo"})
            title_tag = "h2"

        else:
            result_block = soup.find_all("div", attrs={"class": "g"})
            title_tag = "h3"

        # print(len(result_block))
        # print(result_block[0])
        if len(result_block) == 0:
            start += 1
        else:
            for result in result_block:
                # Find link, title, description
                link = result.find("a", href=True)
                title = result.find(title_tag)
                if engine == "bing":
                    description_box = result.find("p")
                else:
                    description_box = result.find("div", {"style": "-webkit-line-clamp:2"})

                description = description_box.text if description_box else ""

                if link and title:
                    start += 1
                    if advanced:
                        yield SearchResult(link["href"], title.text, description)
                    else:
                        yield link["href"]
        sleep(sleep_interval)

        if start == 0:
            return []
