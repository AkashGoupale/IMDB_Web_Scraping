import json
from  pprint import pprint
from task4 import scrape_movie_details

with open("task1.json","r") as p:
    d=json.load(p)
movies=[]
for i in range(10):
    x=(scrape_movie_details((d[i]["url"])))
    movies.append(x)
def analyse_movies_genre(movies):
    mo_genre={}
    for i in movies:
        for y in i['genre']:
            if y in mo_genre:
                mo_genre[y]+=1
            else:
                mo_genre[y]=1
    pprint(mo_genre)
            
analyse_movies_genre(movies)