import json
from task5 import get_movie_list_details
from pprint import pprint

with open("task5.json","r") as p:
    d=json.load(p)
# movies_list=get_movie_list_details
def analyse_movies_language():
    dic={} 
    for i in d:
        for y in i['language']:
            if y in dic:
                dic[y]+=1
            else:
                dic[y]=1
    return dic
x=analyse_movies_language()
with open("task6.json","w") as p:
    json.dump(x,p,indent=4)

