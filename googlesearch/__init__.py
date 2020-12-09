from requests import get
from bs4 import BeautifulSoup
import pandas as pd

class gSearch(object):
    """docstring for gSearch"""
    def __init__(self, arg):
        super(gSearch, self).__init__()
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

        self.get_base_url()

    def get_base_url(self):
        if self.cate == 'all':
            self.base_url = 'https://www.google.com/search?q={}&num={}&hl={}' 

        elif self.cate == 'news':
            self.base_url = 'https://www.google.com/search?q={}&num={}&hl={}&tbm=nws' 


    def fetch_results(self, search_term):
        if isinstance(search_term, (list, tuple)):
            escaped_search_term = '+'.join(search_term)
        else:
            escaped_search_term = search_term.replace(' ', '+')

        google_url = self.base_url.format(escaped_search_term, self.num_results+1,self.lang)
        #print(google_url)
        response = get(google_url, headers=self.usr_agent)
        response.raise_for_status()

        return response.text

    def parse_results(self, raw_html):
        soup = BeautifulSoup(raw_html, 'html.parser')
        if self.cate == 'all':
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
                    print(title.text, desc.text, link['href'])
                    yield [title.text, desc.text, link['href']]
        elif self.cate =='news':
            result_block = soup.find_all('g-card')
            for result in result_block:
                link = result.find('a', href=True)
                title = result.find('div', attrs={'class': 'JheGif nDgy9d'})
                desc = result.find('div', attrs={'class': 'Y3v8qd'})
                src = result.find('div', attrs={'class': 'XTjFC WF4CUc'})

                #print('>> link <<',link)
                #print('>> title <<',title)
                #print('>> desc <<',desc)
                #print('>> src <<', src)


                if link and title and desc:
                    #print('-----------------------------------------------')
                    #print(title.text, desc.text, link['href'], src.text)
                    #raise
                    yield [title.text, desc.text, src.text, link['href']]


    def search(self, term, outform='df'):
        html = self.fetch_results(term)
        records = list(self.parse_results(html))
        #print('////////////////////////////////////////////////////////////////////////////////////')
        #print(records)

        if outform == 'df':
            if self.cate == 'all':
                rtn = pd.DataFrame(records, columns = ['TITLE','DESC','LINK'])
            elif self.cate == 'news':
                rtn = pd.DataFrame(records, columns = ['TITLE','DESC','SRC','LINK'])
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
        'lang': 'en',
        'cate': 'news',
    }
    gs = gSearch(conditions)
    out = gs.search('Google')
    print(out)
