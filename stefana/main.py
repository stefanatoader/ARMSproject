#!/usr/bin/python3

from curlCPU import CurlCPU
from bs4 import BeautifulSoup
import urllib.parse
from bs4 import BeautifulSoup
import re
import urllib.request
import sqlite3
import time
import random

# def main():
#     link_search = "https://www.ultimate-guitar.com/search.php?search_type=title&value="
#     word_search = "drake gods plan"
#     search = link_search + urllib.parse.quote_plus(word_search)
#     curl = CurlCPU(search, "stefana")
#     curl.access()
#
#     soup = BeautifulSoup(curl.buffer, "lxml")
#     link_container = soup.find_all("script")
#
#     for x in link_container:
#         if re.search("window.UGAPP.store.page", x.text):
#             raw_data = x.text.strip().replace("window.UGAPP.store.page = ", "")
#             # linkurile necesare sunt in "tab_url"
#             print(raw_data)


content_regex=re.compile(r"{\"wiki_tab\":{\"content\":\"(.*)\",\"revision_id\"")
tab_finder=re.compile(r"\"tab_url\":\"([^\"]*)\",\"type_name\":\"Chords\"")



def scrape_link(link):
    try:
        response = urllib.request.urlopen(link).read()
        # print(response.decode("utf-8"))
        return get_content(response.decode("utf-8"))
    except Exception as e:
        print("Eroare -> ", e)
        print(e.with_traceback())


def get_content(data):
    content=re.findall(content_regex,data)
    return content

def get_link(name, title):
    link_search = "https://www.ultimate-guitar.com/search.php?search_type=title&value="
    word_search = name+" "+title
    search = link_search + urllib.parse.quote_plus(word_search)
    curl = CurlCPU(search, "stefana")
    curl.access()

    soup = BeautifulSoup(curl.buffer, "lxml")
    link_container = soup.find_all("script")

    #build the regex for the tab_url



    for x in link_container:
        if re.search("window.UGAPP.store.page", x.text):
            raw_data = x.text.strip().replace("window.UGAPP.store.page = ", "")
            # linkurile necesare sunt in "tab_url"
            # print(raw_data)
            try:
                linka=re.findall(tab_finder,raw_data)[0]
                linka=linka.replace("\\","")
                return linka
            except Exception as e:
                print(e)
                return "$@$"


def read_songs_file(file_name):
    song_list=[]
    try:
        file=open(file_name,'r')
        for row in file:
            song_list.append(row)
        return song_list
    except Exception as e:
        print(e.with_traceback())

# get_link("drake","gods plan","h")
# read_songs_file("tops/best-alternative-songs.txt")
count=0
def insert_by_genre(cursor,count,file, genre):

    song_list=read_songs_file(file)
    for song in song_list:

        song_title_author=song.split(" - ")
        link=get_link(song_title_author[1],song_title_author[0])
        if link!="$@$":
            content=scrape_link(link)

            # print(song_title_author[1][:-1])
            # print(song_title_author[0])
            # print(genre)
            # print(content)
            count = count + 1
            delay = random.randint(0, 3)
            print("delay= " + str(delay) + " s")
            print("id= " + str(count))
            print()


            time.sleep(delay)

            cursor.execute("insert into music values (?,?,?,?,?)",(count,song_title_author[1],song_title_author[0],genre, content[0]))

    return count

conn = sqlite3.connect('music.db')
c = conn.cursor()


# count=insert_by_genre(c,count,"tops/best-alternative-songs.txt","alternative")
# conn.commit()
count=82
# count=insert_by_genre(c,count,"tops/metal-songs.txt","metal")
# conn.commit()
count=insert_by_genre(c,count,"tops/rap-songs.txt","rap")
conn.commit()
count=insert_by_genre(c,count,"tops/best-pop-songs.txt","pop")
conn.commit()
