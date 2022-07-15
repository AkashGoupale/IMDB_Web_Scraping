from task4 import scrape_movie_details
from task5 import get_movie_list_details
import json
from pprint import pprint

with open("task1.json","r") as p:
    d=json.load(p)
movies=[]
for i in range(10):
    movies.append(d[i]["url"])
# print(movies)
# 
def analyse_language_and_directors(movies):
    director_dic={}
    movies_li=[]
    for i in movies:
        movie_list=scrape_movie_details(i)
        movies_li.append(movie_list)
    direc=[]
    for m in movies_li:
        for y in m['director']:
            direc.append(y)
    for dira in direc:
        langu={}
        for new in movies_li:
            if dira in new['director']:
                for lang in new['language']:
                    if lang not in langu:
                        langu[lang]=1
                    else:
                        langu[lang]+=1
        director_dic[dira]=langu
    return (director_dic)
x=analyse_language_and_directors(movies)
with open("task10.json","w") as p:
    json.dump(x,p,indent=4)