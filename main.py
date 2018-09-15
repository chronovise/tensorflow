import articlegrabber as ag
import random as rand

save = open("save.txt")

state_new = False

if save.read() == "none":
    state_new = True

star_articles = ag.getStarArticles()
nyt_articles = ag.getNYTArticles()


delete_words = ["and", "or", "for", "by", "above", "below",
                "is", "a", "an", "the", "of", "then", "as", "our", "my",
                "has", "had", "won't", "can't", "willn't", "in", "on", 
                "was", "he", "she", "were", "are", "after", "before",
                "could", "would"]

news_feed = []

star_articles_length = len(star_articles)
nyt_articles_length = len(nyt_articles)

def getNewsFeed():
    
    if state_new:
        for i in range(0,3):
            x = randint(0,star_articles_length)
            news_feed.append(star_articles[x])
            star_articles_length.remove(star_articles[x])
            
            y = randint(0, nyt_articles_length)
            news_feed.append(nyt_articles[y])
            nyt_articles_length.remove(nyt_articles[y])


def main():
    ag.printArticle(star_articles)
    print("-----------------------------------------------")
    ag.printArticle(nyt_articles)

main()
