import requests


def country_headlines(country):
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=' + country + '&'
           'apiKey=f5b8df00fbc34645b92e985a0e575e29')
    response = requests.get(url)
    return response.json()


def specific_source(source):
    url = ('https://newsapi.org/v2/top-headlines?'
           'sources=' + source + '&'
           'apiKey=f5b8df00fbc34645b92e985a0e575e29')
    response = requests.get(url)
    return response.json()


def news_category(country, category):
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=' + country + '&'
           'category=' + category + '&'
           'apiKey=f5b8df00fbc34645b92e985a0e575e29')
    response = requests.get(url)
    return response.json()


def news_about(about):
    url = ('https://newsapi.org/v2/top-headlines?'
           'q=' + about + '&'
           'apiKey=f5b8df00fbc34645b92e985a0e575e29')
    response = requests.get(url)
    return response.json()


def sources():
    url = ('https://newsapi.org/v2/sources?'
           'apiKey=f5b8df00fbc34645b92e985a0e575e29')
    response = requests.get(url)
    return response.json()
