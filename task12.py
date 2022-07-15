import json,requests
from pprint import pprint
from bs4 import BeautifulSoup

with open("task1.json","r") as p:
    d=json.load(p)
# li=[]
# for i in range(10):
#     x=d[i]['url']+"fullcredits?ref=ttcl_sm#cast"
#     li.append(x)


def scrape_movie_cast(movie_cast):
        cast=requests.get(movie_cast)
        soup=BeautifulSoup(cast.text,"html.parser")
        info=soup.find("table",class_="cast_list")
        cast1=info.find_all("tr")
        imdb_list=[]
        for t in cast1:
            td=t.find("td",class_="")
            if td!=None:
                cast_dict={}
                name=td.find("a").text
                imdb_id=td.find("a")["href"][6:15]
                cast_dict["name"]=name.strip()
                cast_dict["imdb_id"]=imdb_id
                imdb_list.append(cast_dict)
        return imdb_list
# a=[]
# for i in li:
scrape_movie_cast(d[0]['url']+"fullcredits?ref=ttcl_sm#cast")
#     a.append(x)
# pprint(a)
