import re
import urllib2

import BeautifulSoup as BS

if __name__ == '__main__':
    url = "https://scrapebook22.appspot.com/"
    page = urllib2.urlopen(url).read()
    soup = BS.BeautifulSoup(page)
    links = soup.table.findAll("a")

    with open("data_scrape.csv", "w") as f:


        for link in links:
            person_url = url + link["href"]
            user_page = urllib2.urlopen(person_url).read()
            user_soup = BS.BeautifulSoup(user_page)



            email = user_soup.ul.find("span", attrs={"class":"email"}).text
            city = user_soup.ul.find("span", attrs={"data-city":True}).text
            gender = user_soup.ul.find("span", attrs={"data-gender":True}).text
            name = user_soup.findAll("h1")[1].text

            age_text = user_soup.ul.find("li", text=re.compile("(Age)"))
            age = re.findall(r" (\d+)",age_text)[0]

            line = ",".join([name, email, city, gender, age])

            "\n".join(line)
            f.write(line+"\n")

