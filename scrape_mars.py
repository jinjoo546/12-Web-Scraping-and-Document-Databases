#Dependencies
from bs4 import BeautifulSoup 
from splinter import Browser
import pandas as pd 
import requests 
import pymongo

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.mars_db
mars_info = db.mars_info

def init_browser(): 
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return browser = Browser('chrome', **executable_path, headless=False)

mars = {}

#Mars News
def scrape_mars_news():
    try: 

        # Initialize browser 
        browser = init_browser()

        # Visit Nasa news url through splinter module
        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)

        # HTML Object
        html = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.find('div', class_='content_title').find('a').text
        p = soup.find('div', class_='article_teaser_body').text

        mars['title'] = title
        mars['paragraph'] = p

        return mars

    finally:

        browser.quit()

#Image
def scrape_mars_image():

    try: 

        # Initialize browser 
        browser = init_browser()

        # Visit Mars Space Images through splinter module
        image_url_featured = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(image_url_featured)

        # HTML Object 
        html_image = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html_image, 'html.parser')

        featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

        main_url = 'https://www.jpl.nasa.gov'

        featured_image_url = main_url + featured_image_url

        featured_image_url 

        mars['featured_image_url'] = featured_image_url 
        
        return mars
    finally:

        browser.quit()

#Mars Weather 
def scrape_mars_weather():

    try: 

        # Initialize browser 
        browser = init_browser()

        # Visit Mars Weather Twitter through splinter module
        weather_url = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(weather_url)

        # HTML Object 
        html_weather = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html_weather, 'html.parser')

        mars_weather = tweet_soup.find('p', class_='TweetTextSize').text
        return mars_weather
        
    
        mars['weather_tweet'] = weather_tweet
        
        return mars
    finally:

        browser.quit()

#Mars Facts
def scrape_mars_facts():

    # Visit Mars facts url 
    url = 'http://space-facts.com/mars/'

    facts = pd.read_html(url)

    df = facts[0]

    data = df.to_html()

    mars['facts'] = data

    return mars

#MARS HEMISPHERES

def scrape_mars_hemispheres():

    try: 

        # Initialize browser 
        browser = init_browser()

        # Visit hemispheres website through splinter module 
        hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemispheres_url)

        # HTML Object
        html_hemispheres = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html_hemispheres, 'html.parser')

        items = soup.find_all('div', class_='item')

        hiu = []

        hemispheres_main_url = 'https://astrogeology.usgs.gov' 

        # Loop through items
        for i in items: 
            title = i.find('h3').text
            
            img_url = i.find('a', class_='itemLink product-item')['href']
            
            browser.visit(main_url + img_url)
            
            img_html = browser.html
            
            soup = BeautifulSoup(img_html, 'html.parser')
            
            img_url = main_url + soup.find('img', class_='wide-image')['src']
            
            hiu.append({"title" : title, "img_url" : img_url})

        mars['hiu'] = hiu

        return mars
    finally:

        browser.quit()    