import json
import sys

from bs4 import BeautifulSoup
import requests

def get_wall_json(username):
    wall_data = []
    username = username
    auth = 'AAAAAAITEghMBAAyE0sfOhpR18ZBHQJfbqT3vN4K17ETza3UOxb5XWW2lW6SZCtHqHU2Bff3BxuZC4ZCszZBhU2HLKZCQOYY3m6QVQ5ktV7hQketi9pb4r3'
    wall = json.loads(requests.get('https://graph.facebook.com/' + username + '/feed?access_token=' + auth).text)
    wall_data.extend(wall['data'])
    next = wall['paging']['next']

    for i in range(9):
        wall = json.loads(requests.get(next).text)
        wall_data.extend(wall['data'])
        next = wall['paging']['next']



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Please include a valid username.'
    else:
        get_wall_json(sys.argv[1])