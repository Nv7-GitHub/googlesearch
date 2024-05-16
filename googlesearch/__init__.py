"""googlesearch is a Python library for searching Google, easily."""

from time import sleep
from bs4 import BeautifulSoup
from requests import get
from .user_agents import get_useragent
import urllib


def _req(term, results, lang, start, proxies, timeout, safe, ssl_verify):
    resp = get(
        url="https://www.google.com/search",
        headers={"User-Agent": get_useragent()},
        params={
            "q": term,
            "num": results + 2,  # Prevents multiple requests
            "hl": lang,
            "start": start,
            "safe": safe,
        },
        proxies=proxies,
        timeout=timeout,
        verify=ssl_verify,
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


def search(
    term, num_results=10, lang="en", proxy=None, advanced=False, sleep_interval=0, timeout=5, safe="active", ssl_verify=None
):
    """Search the Google search engine"""

    escaped_term = urllib.parse.quote_plus(term)  # make 'site:xxx.xxx.xxx ' works.

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
        resp = _req(escaped_term, num_results - start, lang, start, proxies, timeout, safe, ssl_verify)

        # Parse
        soup = BeautifulSoup(resp.text, "html.parser")
        with open("output.html", "w") as f:
            f.write(resp.text)

        result_block = soup.find_all("div", attrs={"class": "g"})
        if len(result_block) == 0:
            print("Result block empty")
            start += 1
        for result in result_block:

            # Find link. If link is not found, we skip the result because this is the only necessary output
            link = result.find("a", href=True)
            if not link:
                continue
            link = link["href"]

            # Find title. If title is not found, we use the link as the title
            title = result.find("h3")
            if not title:
                title = link
            else:
                title = title.text

            # Find description. If description is not found, we attempt to reconstruct it by searching and combining spans.
            # These messy descriptions are not perfect, but they're adequate when scraping results for AI agents.
            description_box = result.find("div", {"style": "-webkit-line-clamp:2"})
            description = description_box.text if description_box else None
            if not description_box:
                description_box_candidates = result.find_all("span")
                # The description almost always has an <em> tag in it, so we use that as a heuristic to find the description
                spans_with_em_child = [
                    candidate for candidate in description_box_candidates if candidate.find("em", recursive=False)
                ]
                if len(spans_with_em_child) > 0:
                    description_box = spans_with_em_child[0]
                    description = description_box.text
                # If we can't find an <em> tag, we just concatenate all the spans
                else:
                    description = "".join([span.text for span in result.find_all("span")[5:]])
                    description = description.replace(title.text, "", 1)

            if advanced:
                yield SearchResult(link, title, description)
            else:
                yield link
        sleep(sleep_interval)

        if start == 0:
            return []
