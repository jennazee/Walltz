import json
import sys
import string

from bs4 import BeautifulSoup
import requests
from nltk import Text, word_tokenize

def get_wall_data(username):
    wall_data = []
    username = username
    auth = [snip]
    wall = json.loads(requests.get('https://graph.facebook.com/' + username + '/feed?access_token=' + auth).text)
    wall_data.extend(wall['data'])
    next = wall['paging']['next']

    for i in range(9):
        wall = json.loads(requests.get(next).text)
        wall_data.extend(wall['data'])
        next = wall['paging']['next']

    return wall_data

def get_posts(wall_data):
    posts = []
    for post in wall_data:
        try:
            post['message']
        except KeyError:
            continue
        else:
            posts.append(post['message'].strip('.'))

    return string.join(posts, '. ')

def make_poetry(corpus):
    print corpus
    tokens = word_tokenize(corpus)
    text = Text(tokens)
    return text.generate()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Please include a valid username.'
    else:
        make_poetry(get_posts(get_wall_data(sys.argv[1])))