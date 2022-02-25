#!/usr/bin/env python3
"""
googlesearch - A Python library for scraping the Google search engine.
"""

from typing import Any, Dict, Iterator, Optional, Union

import requests
from bs4 import BeautifulSoup

USER_AGENT = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}


def search_request(
    term: str, results: int, lang: str, start: int, proxies: Optional[Dict[Any, Any]] = None
) -> requests.Response:
    resp = requests.get(
        url="https://www.google.com/search",
        headers=USER_AGENT,
        params={  # type: ignore
            "q": term,
            "num": results + 2,  # Prevents multiple requests
            "hl": lang,
            "start": start,
        },
        proxies=proxies,
    )
    resp.raise_for_status()
    return resp


class SearchResult:
    def __init__(self, url: str, title: str, description: str):
        self.url = url
        self.title = title
        self.description = description

    def __repr__(self) -> str:
        return f"SearchResult(url={self.url}, title={self.title}, description={self.description})"


def search(
    term: str,
    num_results: int = 10,
    lang: str = "en",
    proxy: str = None,
    advanced: bool = False,
) -> Iterator[Union[SearchResult, str]]:
    escaped_term = term.replace(" ", "+")

    # Proxy
    proxies = None
    if proxy:
        if proxy[:5] == "https":
            proxies = {"https": proxy}
        else:
            proxies = {"http": proxy}

    # Fetch
    start = 0
    while start < num_results:
        # Send request
        resp = search_request(escaped_term, num_results - start, lang, start, proxies)

        # Parse
        soup = BeautifulSoup(resp.text, "html.parser")
        result_block = soup.find_all("div", attrs={"class": "g"})
        for result in result_block:
            # Find link, title, description
            link = result.find("a", href=True)
            if link and link.get("href"):
                link = link["href"]
            start += 1
            if not advanced:
                yield link
            else:
                title = result.find("h3")
                description_box = result.find("div", {"style": "-webkit-line-clamp:2"})
                if description_box:
                    description = description_box.find("span")
                    if link and title and description:
                        yield SearchResult(link, title.text, description.text)
