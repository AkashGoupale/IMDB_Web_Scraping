# from task4 import scrape_movie_details
# import json,os,requests
# from pprint import pprint
# from bs4 import BeautifulSoup

# with open("task1.json") as p:
#     d=json.load(p)

# # 
# def scrape_movie_details(url):
#     text=None
#     file_name=url[28:-1]+".json"
#     print(file_name)
#     if os.path.exists("movie_details/"+file_name):
#         f=open("movie_details/"+file_name)
#         text=f.read()
#         f.close()
#         return text

#     if text is None:
#         dict1={}
#         page= requests.get(url)
#         soup=BeautifulSoup(page.text,"html.parser")
#         name=soup.find("h1", attrs={"data-testid":"hero-title-block__title"}).text
#         dict1["name"]=name
#         g=[]
#         director_name=soup.find('div', class_="ipc-metadata-list-item__content-container")
#         x=director_name.find_all("li",class_="ipc-inline-list__item")
#         for i in x:
#             g.append(i.a.get_text()) 
#         dict1["director"]=g
#         country_name=soup.find("li",attrs={"data-testid":"title-details-origin"}).find("a").text
#         dict1["country"]=country_name
#         j=[]
#         language_name=soup.find("li",attrs={"data-testid":"title-details-languages"})
#         x=language_name.find_all("li",class_="ipc-inline-list__item")
#         for i in x:
#             j.append(i.a.get_text())
#         dict1["language"]=j
#         poster_image_url=soup.find("img",class_="ipc-image")["src"]
#         dict1["poster"]=poster_image_url
#         bio=soup.find("span",attrs={"data-testid":"plot-xs_to_m"}).text
#         dict1["bio"]=bio
#         genre=soup.find("li",attrs={"data-testid":"storyline-genres"})
#         Genre=genre.find_all("a")
#         h=[]
#         dict1["genre"]=h
#         for i in Genre:
#             l=i.text
#             h.append(l)
#         run_time=soup.find("li",attrs={"data-testid":"title-techspec_runtime"}).text.strip("Runtime")
#         w=run_time.split(" ")
#         if len(w)==4:
#             m=int(w[0])*60+int(w[2])
#         else:
#             m=int(m[0])*60
#         dict1["runtime"]=m
        
#         file1=open('movie_details/' + file_name,"w")
#         raw=json.dumps(dict1)
#         file1.write(raw)
#         file1.close()
#         return (dict1)
# for i in range(5):
#     url=d[i]['url']
#     g=scrape_movie_details(url)
#     pprint(g)

