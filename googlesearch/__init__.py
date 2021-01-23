#!/usr/bin/env python3

from itertools import chain
from typing import Generator, List
from urllib.parse import urlencode

import attr
from bs4 import BeautifulSoup
from requests import get

_USR_AGENT = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/61.0.3163.100 Safari/537.36"
    }


@attr.s
class Page:
    num_page: int = attr.ib(kw_only=True)
    content: list[str] = attr.ib(kw_only=True)


@attr.s
class _PageIter:
    search_term: str = attr.ib(kw_only=True)
    results_per_page: int = attr.ib(default=10)
    num_results: int = attr.ib(default=10)
    language_code: str = attr.ib(default="en")

    def _fetch_results(
        self,
        search_term: str,
        results_per_page: int,
        language_code: str,
        start: int = 0
            ) -> str:
        query = urlencode(
                dict(
                    q=search_term,
                    num=results_per_page + 1,
                    hl=language_code,
                    start=start
                )
            )
        google_url = f"https://www.google.com/search?{query}"
        response = get(google_url, headers=_USR_AGENT)
        response.raise_for_status()

        return response.text

    def _parse_results(self, raw_html) -> Generator[str, None, None]:
        soup = BeautifulSoup(raw_html, "lxml")
        result_block = soup.find_all("div", attrs={"class": "g"})

        for result in result_block:
            link = result.find("a", href=True)
            title = result.find("h3")

            if link and title and link["href"] != "#"\
                    and not link["href"].startswith("/"):
                yield link["href"]

    def _search(self) -> List[str]:
        result = List(
            self._parse_results(
                raw_html=self._fetch_results(
                    search_term=self.search_term,
                    results_per_page=self.results_per_page,
                    language_code=self.language_code,
                    start=self.start
                )
            )
        )
        return result

    def __iter__(self):
        self.start = 0
        self.num_page = 0
        return self

    def __next__(self) -> Page:
        cond = self.start < self.num_results
        if self.num_results == -1:
            cond = True

        result = self._search()
        if cond and len(result) > 0:
            page_obj = Page(num_page=self.num_page, content=result)

            self.start += len(result)
            self.num_page += 1
        else:
            raise StopIteration
        return page_obj


def search(term, results_per_page=100, num_results=100, lang="en"):
    page_iter = _PageIter(
        search_term=term,
        results_per_page=results_per_page,
        num_results=num_results,
        language_code=lang
    )
    it_page_iter = iter(page_iter)
    page_results_list = list(it_page_iter)
    results_list = [r.content for r in page_results_list]
    flatten_results_list = list(chain(*results_list))
    return flatten_results_list
