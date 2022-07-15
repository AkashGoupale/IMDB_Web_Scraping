import json  
from task4 import scrape_movie_details
from pprint import pprint 
with open("task5.json") as p:
    d=json.load(p)

# def analyse_movies_directors():
#     dic={}
#     for i in d:
#         for y in i['director']:
#             if y in dic:
#                 dic[y]+=1
#             else:
#                 dic[y]=1
#     pprint(dic)
# analyse_movies_directors()

