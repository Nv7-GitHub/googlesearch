from bs4 import BeautifulSoup
from requests import get

usr_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

def _req(term, results, lang, start, proxies):
    resp = get(
        url="https://www.google.com/search",
        headers=usr_agent,
        params=dict(
            q = term,
            num = results + 2, # Prevents multiple requests
            hl = lang,
            start = start,
        ),
        proxies=proxies,
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

def search(term, num_results=10, lang="en", proxy=None, advanced=False):
    escaped_term = term.replace(' ', '+')

    # Proxy
    proxies = None
    if proxy:
        if proxy[:5]=="https":
            proxies = {"https": proxy} 
        else:
            proxies = {"http": proxy}
    
    # Fetch
    start = 0
    while start < num_results:
        # Send request
        resp = _req(escaped_term, num_results-start, lang, start, proxies)

        # Parse
        soup = BeautifulSoup(resp.text, 'html.parser')
        result_block = soup.find_all('div', attrs={'class': 'g'})
        for result in result_block:
            # Find link, title, description
            link = result.find('a', href=True)
            title = result.find('h3')
            description_box = result.find('div', {'style': '-webkit-line-clamp:2'})
            if description_box:
                description = description_box.find('span')
                if link and title and description:
                    start += 1
                    if advanced:
                        yield SearchResult(link['href'], title.text, description.text)
                    else:
                        yield link['href']

