# from pprint import pprint
# import requests
# from bs4 import BeautifulSoup
# import json
# url='https://www.imdb.com/india/top-rated-indian-movies/'
# data=requests.get(url)
# soup=BeautifulSoup(data.text,'html.parser')

# def scrape_top_list():
    
#     tbody=soup.find('tbody',class_='lister-list')
#     trs=tbody.find_all('tr')
#     # return trs
#     movie_rank=[]
#     movie_name=[]
#     movie_release=[]
#     movie_url=[]
#     movie_rating=[]
#     details=[]
#     for tr in trs:
#         position=tr.find('td',class_='titleColumn').get_text().strip()
#         td=tr.find('td',class_='titleColumn')
#         rank=" "
#         for i in position:
#             if "." not in i:
#                 rank=rank+i
#             else:
#                 break
#         movie_rank.append(int(rank))
#     # return movie_rank
#         name=tr.find('td',class_='titleColumn').a.get_text()
#         movie_name.append(name)
#     # return movie_name
#         date=tr.find('td',class_='titleColumn').span.get_text()
#         movie_release.append(int(date[1:5]))
#     # return movie_release
#         rating=tr.find('td',class_='ratingColumn imdbRating').strong.get_text()
#         movie_rating.append(float(rating))
#     # return movie_rating
#         link=tr.find("td",class_='titleColumn').a['href']
#         print(link)
#         linked=url[0:21]+link
#         # print(linked)
#         movie_url.append(linked)
    # return movie_url
    # detail={"name":"","position":"","year":"","rating":"","url":""}
    # for i in range(len(movie_name)):
    #     detail["name"]=movie_name[i]
    #     detail["position"]=movie_rank[i]
    #     detail["year"]=movie_release[i]
    #     detail["rating"]=movie_rating[i]
    #     detail["url"]=movie_url[i]
    #     details.append(detail)
    #     detail={"name":"","position":"","year":"","rating":"","url":""}
    # return details
# x=scrape_top_list()
# # pprint(x)
# with open("task1.json","w") as p:
#     json.dump(x,p,indent=4)
