# d={'2021':[{"hj":67},{"gh":776}],"1999":[{"jh":67},{"hg":676}],"1995":[{"hg":76},{"hj":77}],"2027":[{"h":66},{"hg":77}]}
import json
from pprint import pprint


with open("task2.json","r") as p:
    d=json.load(p)
def group_by_decade():
    k={}
    l=[]
    b=sorted([x for x in d])
    g=str(b[0])
    h=g[0:3]+"0"
    x=int(h)
    for z in d:
        if x<=int(b[-1]):
            for i in range(x,x+10):
                if str(i) in d:
                    for z in d[str(i)]:
                        l.append(z)
            k[x]=l
            l=[]
            x+=10
    return k
p=group_by_decade()
# pprint(p)
with open("task3.json","w") as m:
    json.dump(p,m,indent=4)





