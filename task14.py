from task4 import scrape_movie_details
from task12 import scrape_movie_cast
import json
from pprint import pprint


with open("task1.json","r") as var:
    url=json.load(var)


def analyse_co_actors(url2):
    main_dict={}
    x=scrape_movie_details(url2)    
    movie_link=url2+"fullcredits/?ref_=tt_cl_sm"
    a=scrape_movie_cast(movie_link)
    for k in a[:5]:
        if k['imdb_id'] not in x:
            x[k['imdb_id']] = {"name": k['name'],'frequent_co_actors': []}
            fc = x[k['imdb_id']]['frequent_co_actors']
            for k2 in a:
                fc.append({'imdb_id': k2['imdb_id'], "name": k2['name'], "num_movies": 1})
        else:
            fc = x[k['imdb_id']]['frequent_co_actors']
            for k2 in a:
                for kf in fc:
                    if k2['imdb_id'] == kf['imdb_id']:
                        kf['num_movies']+=1
                        break
                else:
                    fc.append({'imdb_id': k2['imdb_id'], "name": k2['name'], "num_movies": 1})
    pprint(fc)
url2=url[0]['url']
analyse_co_actors(url2)