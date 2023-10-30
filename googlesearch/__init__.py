"""googlesearch is a Python library for searching Google, easily."""
from time import sleep
from bs4 import BeautifulSoup
from requests import get
from .user_agents import get_useragent
import urllib


def _req(term, results, lang, start, proxies, timeout):
    resp = get(
        url="https://www.google.com/search",
        headers={
            "User-Agent": get_useragent()
        },
        params={
            "q": term,
            "num": results,
            "hl": lang,
            "start": start,
        },
        proxies=proxies,
        timeout=timeout,
    )

    resp.raise_for_status()
    return resp

class SearchResult:
    def __init__(self, url, title, description, is_sponsored):
        self.url = url
        self.title = title
        self.description = description
        self.is_sponsored = is_sponsored

    def __repr__(self):
        if self.is_sponsored:
            return f"SearchResult(url={self.url}, title={self.title}, description={self.description}, is_sponsored={self.is_sponsored})"
        else:
            return f"SearchResult(url={self.url}, title={self.title}, description={self.description})"
   
def search(term, sponsored=False, num_results=10, lang="en", proxy=None, advanced=False, sleep_interval=0, timeout=5):
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
        resp = _req(escaped_term,num_results - start,
                    lang, start, proxies, timeout)

        # Parse
        soup = BeautifulSoup(resp.text, "html.parser")

        # Check for sponsored results
        if sponsored:
            sponsored_block = soup.find_all("div", attrs={"class": "vdQmEd"})
            if len(sponsored_block) == 0:
                start += 1
            for sponsored_result in sponsored_block:
                link = sponsored_result.find("a", href=True,attrs={"class":"sVXRqc"}).get("href")
                title = sponsored_result.find("span", attrs={"class":"OSrXXb"})
                description_box = sponsored_result.find(lambda tag: tag.name == 'span' and not tag.has_attr('class'))

                if description_box:
                    description = description_box.text
                    if link and title and description:
                        start += 1
                        if advanced:
                            yield SearchResult(link, title.text, description, True)
                        else: 
                            yield link
                            
        # Check for not sponsored results           
        result_block = soup.find_all("div", attrs={"class": "g"})
        if len(result_block) == 0:
            start += 1
        for result in result_block:
            # Find link, title, description
            link = result.find("a", href=True).get("href")
            title = result.find("h3")
            description_box = result.find(
                "div", {"style": "-webkit-line-clamp:2"})

            if description_box:
                description = description_box.text
                if link and title and description:
                    start += 1
                    if advanced:
                        yield SearchResult(link, title.text, description, False)
                    else:
                        yield link
                    
        sleep(sleep_interval)

        if start == 0:
            return []