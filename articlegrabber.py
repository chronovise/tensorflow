from bs4 import BeautifulSoup
import urllib.request

def printArticle(articles):
    for i in articles:
        print(articles[i])

def getNYTArticles():
    titles = []
    hyperlinks = []
    nyt_articles = []

    website = "https://nytimes.com/"

    source = urllib.request.urlopen(website).read()

    soup = BeautifulSoup(source, "html.parser")

    articles = soup.find_all("a")

    for url in articles:
        if not url.h2 == None:
            nyt_articles.append([url.h2.text, "https://nytimes.com"+url['href']])

    return nyt_articles

def getStarArticles():
    ids = []
    titles = []
    hyperlinks = []
    star_articles = []
    
    website = "https://www.thestar.com/"

    source = urllib.request.urlopen(website).read()

    soup = BeautifulSoup(source, "html.parser")

    article_titles = soup.find_all("span", {"class": "story__headline"})

    urls = soup.find_all("a", href=True)

    for title in article_titles:
        titles.append(title.text)
        ids.append(title["data-reactid"])

    for url in urls:
        if ((str)((int)(url['data-reactid'])+1)) in ids:
            hyperlinks.append(website+url['href'])

    for i in range(0,len(titles)-1):
        star_articles.append([titles[i], hyperlinks[i]])
    

    return star_articles

