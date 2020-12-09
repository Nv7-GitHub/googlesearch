from requests import get
from bs4 import BeautifulSoup

class gSearch(object):
    """docstring for Gsearch"""
    def __init__(self, arg):
        super(Gsearch, self).__init__()
        try:
            self.num_results = arg['num_results']
        except:
            self.num_results = 10
        try:
            self.lang = arg['lang']
        except:
            self.lang = 'en'
        try:
            self.cate = arg['cate']
        except:
            self.cate = 'all'

        self.usr_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/61.0.3163.100 Safari/537.36'}

        self.base_url = self.get_base_url()
        
    def get_base_url(self):
        if self.cate == 'all':
            self.base_url = 'https://www.google.com/search?q={}&num={}&hl={}' 
        elif self.cate == 'news':
            self.base_url = 'https://www.google.com/search?q={}&num={}&hl={}&tbm=nws' 

    def fetch_results(self, search_term):
        if isinstance(search_term, list):
            escaped_search_term = '+'.join(search_term)
        else:
            escaped_search_term = search_term.replace(' ', '+')

        google_url = self.base_url.format(escaped_search_term, number_results+1,language_code)
        response = get(google_url, headers=usr_agent)
        response.raise_for_status()

        return response.text

    def parse_results(self, raw_html):
        soup = BeautifulSoup(raw_html, 'html.parser')
        result_block = soup.find_all('div', attrs={'class': 'g'})
        for result in result_block:
            #print(result)
            link = result.find('a', href=True)
            title = result.find('h3')
            desc = result.find('span', attrs={'class': 'aCOpRe'})
            #print('>>link<<',link)
            #print('>>title<<',title)
            #print('>>desc<<',desc)
            #raise
            if link and title and desc:
                yield [title.text, desc.text, link['href']]


    def search(self, term, outform='df'):
        html = self.fetch_results(term, num_results, lang)
        records = list(self.parse_results(html))

        if outform == 'df':
            rtn = pd.DataFrame(records, columns = ['TITLE','DESC','LINK'])
        else:
            rtn = records
        return rtn


if __name__ == '__main__':
    """
    # for test
    rtn = search('Google', num_results = 30)
    print(rtn)
    #"""
    conditions = {
        'num_results': 100,
        'lang': 'en'
        'cate': 'news'
    }
    gs = gSearch(conditions)
    out = gs.search('Delta Airline MOU')
    print(out)