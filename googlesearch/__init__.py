"""googlesearch is a Python library for searching Google, easily."""
from time import sleep
from bs4 import BeautifulSoup
from .user_agents import get_useragent
from typing import List, Dict
import requests


def _req(
    term: str,
    results: int,
    lang: str,
    start: int,
    proxies: Dict[str, str],
    timeout: float,
) -> requests.Response:
    params = {"q": term, "num": results + 2, "hl": lang, "start": start}
    headers = {"User-Agent": get_useragent()}
    with requests.Session() as session:
        session.headers.update(headers)
        resp = session.get(
            "https://www.google.com/search",
            params=params,
            proxies=proxies,
            timeout=timeout,
        )
        resp.raise_for_status()
        return resp


class SearchResult:
    def __init__(self, url: str, title: str, description: str) -> None:
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
    sleep_interval: int = 0,
    timeout: int = 5,
) -> List:
    escaped_term = term.replace(" ", "+")

    proxies = (
        {"https": proxy}
        if proxy and proxy.startswith("https")
        else {"http": proxy}
        if proxy
        else None
    )

    start = 0
    results = []
    while start < num_results:
        resp = _req(escaped_term, num_results - start, lang, start, proxies, timeout)
        soup = BeautifulSoup(resp.text, "html.parser")
        result_block: List[BeautifulSoup] = soup.select("div.g")

        for result in result_block:
            link, title, description = (
                result.find("a", href=True),
                result.select_one("h3"),
                result.select_one('div[style="-webkit-line-clamp:2"]'),
            )

            if link and title and description:
                start += 1
                result_item = (
                    SearchResult(link["href"], title.text, description.text)
                    if advanced
                    else link["href"]
                )
                results.append(result_item)
        sleep(sleep_interval)

        if start == 0:
            break
    return results
