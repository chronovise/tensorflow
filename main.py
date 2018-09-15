import articlegrabber as ag
import random as rand
import pygame
from pygame.locals import *

save = open("save.txt")

state_new = False

(screen_width,screen_height) = (1000,800)

program_name = "Chronovise"
background_colour = (255,255,255)

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
    #initialize the screen width and height
    screen = pygame.display.set_mode([screen_width,screen_height])    
    
    #set the caption/title for the screen
    pygame.display.set_caption(program_name)
    screen.fill(background_colour)

    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False;
                exit()
    
main()
