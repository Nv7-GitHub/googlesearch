import random
import secrets

def _get_useragent():
    """
    Returns a random user agent

    Returns:
        str: Random user agent

    """
    return random.choice([
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.54',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.275',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0 OPR/77.0.4054.277',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.54',
    'Mozilla/5.0 (Windows NT 6.1; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:88.0) Gecko/20100101 Firefox/88.0',
    'Mozilla/5.0 (Windows NT 10.0; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 10.0; rv:88.0) Gecko/20100101 Firefox/88.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.54',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.275',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0 OPR/77.0.4054.277',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'])

def _get_referer():
    """
    Returns a random referer

    Returns:
        str: Random referer

    """
    return random.choice(["https://www.google.com",
                          "https://www.bing.com",
                          "https://www.yahoo.com",
                          "https://www.duckduckgo.com",
                          "https://www.facebook.com",
                          "https://www.twitter.com",
                          "https://www.instagram.com",
                          "https://www.linkedin.com",
                          "https://www.reddit.com",
                          "https://www.stackoverflow.com",
                          "https://www.amazon.com",
                          "https://www.ebay.com",
                          "https://www.netflix.com",
                          "https://www.youtube.com",
                          "https://www.twitch.tv",
                          "https://www.microsoft.com",
                          "https://www.apple.com",
                          "https://www.github.com",
                          "https://www.wikipedia.org", None, None, None, None, None, None, None, None, None, None, None,
                          None, None, None, None, None, None, None, None])


def _get_cookies():
    """
    Returns a random cookie string

    Returns:
        str: Random cookie string

    """
    no = random.randint(2, 5)
    secrets.token_urlsafe(random.randint(8, 15))
    choices = random.choices([f"_ga=GA1.3.{random.randint(100000, 999999)}.{random.randint(100000, 999999)};",
                              f"_ga=GA1.2.{random.randint(100000, 999999)}.{random.randint(100000, 999999)};",
                              "_gat=1;",
                              f"__utma={random.randint(100000, 999999)}.{random.randint(100000, 999999)}.{random.randint(100000, 999999)}.1;",
                              f"__utmb={random.randint(100000, 999999)}.1.10.{random.randint(100000, 999999)};",
                              f"__utmc={random.randint(100000, 999999)};",
                              f"__utmz={random.randint(100000, 999999)}.{random.randint(100000, 999999)}.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none);",
                              f"__utmt={random.randint(1, 6)};",
                              f"session={secrets.token_urlsafe(random.randint(8, 15))};",
                              f"user_session={secrets.token_urlsafe(random.randint(8, 15))};",
                              f"remember_user_token={secrets.token_urlsafe(random.randint(2, 5))}.1234-5678;",
                              f"_csrf_token={secrets.token_urlsafe(random.randint(5, 10))};",
                              f"JSESSIONID={secrets.token_urlsafe(random.randint(6, 9))};",
                              f"login={secrets.token_urlsafe(random.randint(8, 15))}",
                              f"username={randomname._get_name};",
                              f"__RequestVerificationToken={secrets.token_urlsafe(random.randint(8, 15))};",
                              f"ASP.NET_SessionId={secrets.token_urlsafe(random.randint(8, 15))};",
                              f".AspNet.ApplicationCookie={secrets.token_urlsafe(random.randint(8, 15))};",
                              f"AWSALB={secrets.token_urlsafe(random.randint(8, 15))};",
                              f"AWSALBCORS={secrets.token_urlsafe(random.randint(8, 15))};"], k=no)
    return ",".join(choices)


def _get_accept():

    """
    Returns a random accept string

    Returns:

    """
    return random.choice(["text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                          "text/html,application/xhtml+xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                          "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp;q=0.8,*/*;q=0.7",
                          "text/html,application/xhtml+xml;q=0.9,image/apng,image/*,*/*;q=0.8",
                          "text/html,application/xhtml+xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/xml;q=0.7",
                          "text/html,application/xhtml+xml;q=0.8,image/webp,image/apng,*/*;q=0.7,application/xml;q=0.6",
                          "text/html,application/xhtml+xml;q=0.8,image/apng,image/*,*/*;q=0.7,application/xml;q=0.6",
                          "text/html,application/xhtml+xml;q=0.7,image/webp,image/apng,*/*;q=0.8,application/xml;q=0.6",
                          "text/html,application/xhtml+xml;q=0.7,image/webp;q=0.8,image/apng,*/*;q=0.7,application/xml;q=0.6",
                          "text/html,application/xhtml+xml;q=0.6,image/webp,image/apng,*/*;q=0.8,application/xml;q=0.7"])


def _get_language():

    """
    Returns a random language string

    Returns:
        str: Random language string
    """
    return random.choice(["en-GB,en;q=0.9",
                          "en-GB,en;q=0.8,fr;q=0.7,de;q=0.6,es;q=0.5",
                          "en-GB,en-US;q=0.9,en;q=0.8",
                          "en-GB;q=0.9,en;q=0.8,es;q=0.7",
                          "en-GB,en;q=0.8,fr;q=0.7",
                          "en-GB;q=0.9,en;q=0.8,fr;q=0.7,de;q=0.6",
                          "en-GB;q=1.0,en;q=0.9,fr;q=0.8,de;q=0.7,es;q=0.6",
                          "en-GB;q=1.0,en;q=0.9,es;q=0.8",
                          "en-GB;q=1.0,en-US;q=0.9,en;q=0.8,fr;q=0.7,de;q=0.6",
                          "en-GB;q=1.0,en;q=0.9,es;q=0.8,fr;q=0.7"])


def _get_enconding():
    """
    Returns a random encoding string

    Returns:
        str: Random encoding string
    """
    return random.choice(["gzip, deflate, br, *",
                          "br, gzip, *",
                          "gzip, deflate, *",
                          "*"
                          "br, *",
                          "compress, gzip, *",
                          "gzip, *",
                          "deflate, br, *",
                          "gzip, deflate, br, identity, *"])


def get_random_header():
    """
    Returns a random header for a request
    """
    # Get random user agent, referer, cookies, accept, language and encoding
    user_agent = _get_useragent()
    referer = _get_referer()
    cookies = _get_cookies()
    accept = _get_accept()
    language = _get_language()
    encoding = _get_enconding()
    # Create header
    header = {"User-Agent": user_agent,
              "Accept": accept,
              "Accept-Language": language,
              "Accept-Encoding": encoding,
              "Cookies": cookies}
    # Add referer if it exists
    if referer:
        header["Referer"] = referer

    return header