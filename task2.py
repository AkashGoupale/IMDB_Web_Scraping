import json,requests
from bs4 import BeautifulSoup
from pprint import pprint



with open("task1.json","r") as p:
    d=json.load(p)
def group_by_year():
    dic={}
    for i in d:
        year=i['year']
        movie_year=[]
        for y in range(len(d)):
            if year==d[y]['year']:
                movie_year.append(d[y])
        dic[year]=movie_year
    return dic

x=(group_by_year())
with open("task2.json","w") as p:
    json.dump(x,p,indent=4)

























