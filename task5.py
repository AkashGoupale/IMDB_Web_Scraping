import json,requests
from task4 import scrape_movie_details
from bs4 import BeautifulSoup
from pprint import pprint

with open("task1.json","r") as p:
    d=json.load(p)
movies=[]
for i in range(10):
    movies.append(d[i]["url"])

def get_movie_list_details(movies):
    movies_details=[]
    for i in movies:
        movies_details.append(scrape_movie_details(i))
    return (movies_details)
x=get_movie_list_details(movies)
with open("task5.json","w") as m:
    json.dump(x,m,indent=4)

      