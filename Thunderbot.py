import requests
import re
import sys
from pprint import pprint
import json
from random import randint
from bs4 import BeautifulSoup
import BaseHTTPServer
import time
import os
from magicList import *
# Magic* list contains api key and certain other variables, such as responses to questions


insult_urls = ["http://www.gotlines.com/insults/intelligence/", "http://www.gotlines.com/insults/ugly/", "http://www.gotlines.com/insults/ugly/2"]

HOST_NAME = '0.0.0.0' 
PORT_NUMBER = int(os.environ.get('PORT', 9000)) 


def change_nickname():
    ind = original_message.index(':')
    new_nickname = original_message[ind + 1::]
    nickname_post = {'membership': {'nickname': new_nickname}}
    p = requests.post('https://api.groupme.com/v3/groups/13765654/memberships/update?token=' + api_key, json = nickname_post)
    print p.text


def change_groupname():
    ind = original_message.index(':')
    new_groupname = original_message[ind + 1::]
    groupname_post = {'name': new_groupname}
    p = requests.post('https://api.groupme.com/v3/groups/13765654/update?token=' + api_key, json = groupname_post)
    print p.text


def make_post(content):
    bot = {"bot_id" : bot_id, "text": content}
    r = requests.post("https://api.groupme.com/v3/bots/post", params = bot)


def get_food(city):
    global url 
    url = 'https://www.groupon.com/browse/' + city + '?&query=restaurants&locale=en_US'
    try:
        webpage = requests.get(url)
        soup = BeautifulSoup(webpage.content)
        allinks = soup.find_all("div", {"class": "cui-image-container"})
        link_list = []

        for link in allinks:
            if link.parent.get("href"):
                link_list.append(link.parent.get("href"))
        
        rand = randint(0, 2)
        make_post(link_list[rand])
    except IndexError:
        make_post("Not enough deals there bruh")



def get_insult(target):
    url = insult_urls[randint(0, 2)]
    insultpage = requests.get(url)
    soup2 = BeautifulSoup(insultpage.content)
    allinsults = soup2.find_all("a", {"class":"linetext"})
    insult_list = []

    for insult in allinsults:
        if insult.string:
            insult_list.append(insult.string.lower(x))

    rand = randint(0, len(insult_list))
    make_post(target + "," + " " + insult_list[rand])



def get_last_message():

    if 'thunderbot,' in keyword and 'nickname' in keyword and my_id == '8994029':
    	change_nickname()

    elif 'thunderbot,' in keyword and 'groupname' in keyword:
    	change_groupname()

    elif 'thunderbot,' in keyword and '?' in keyword:
    	make_post(magic8_list[randint(0, len(magic8_list))])

    elif 'thunderbot,' in keyword and 'burn heal' in keyword:
    	make_post('http://i187.photobucket.com/albums/x31/neolancer2/Burn.gif')

    elif 'thunderbot,' in keyword and 'online' in keyword:
    	make_post('Sup')

    elif 'thunderbot,' in keyword and 'food' in keyword:
    	indice = original_message.index('in')
    	dirtycity = original_message[indice + 2::].strip()
        city = re.sub(r'[^a-zA-Z\s]',"",dirtycity)
        get_food(city)

    elif 'piers,' in keyword:
    	target_index = original_message.index('insult')
    	target = original_message[target_index + 6::].strip()
        get_insult(target)



class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
        def do_POST(s):
                """Respond to a POST request."""
                s.send_response(200)
                s.send_header("Content-type", "text/html")
                s.end_headers()
                s.wfile.write("Response success")
                
                content_len = int(s.headers.getheader('content-length', 0))
                post_body = s.rfile.read(content_len)
                recentdata = json.loads(post_body)
                global original_message, keyword, my_id
                original_message = recentdata['text']
                keyword = original_message.lower()
                my_id = recentdata['user_id']
                get_last_message()



if __name__ == '__main__':
        server_class = BaseHTTPServer.HTTPServer
        httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
        print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
        try:
                httpd.serve_forever()
        except KeyboardInterrupt:
                pass
        httpd.server_close()
        print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)


