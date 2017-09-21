import urllib2

import BeautifulSoup as BS

if __name__ == '__main__':
    url = "http://quotes.yourdictionary.com/theme/marriage/"
    page = urllib2.urlopen(url).read()
    soup = BS.BeautifulSoup(page)

    love_quote = soup.findAll("p", attrs={"class": "quoteContent"})

    with open("love_quotes.txt", "w") as f:
        for love in love_quote:
            f.write(love.text.encode("utf-8") + "\n")
