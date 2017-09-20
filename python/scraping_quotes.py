import urllib2

import BeautifulSoup as BS

if __name__ == '__main__':
    url = "http://quotes.yourdictionary.com/theme/marriage/"
    page = urllib2.urlopen(url).read()
    soup = BS.BeautifulSoup(page)

    love_quote = soup.findAll("p", attrs={"class": "quoteContent"})


    for love in love_quote:

        print "<3"*5, love, "<3"*5



