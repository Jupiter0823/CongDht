import json
import operator
import libtorrent as lt
import time

def rank():
    jsonObj = open("DHTCrawler/pretty.json")

    dictObj = json.load(jsonObj)

    newdict = {}
    x={}
    for movie, val in dictObj.items():
        newdict.setdefault(val, []).append(movie)


    for val in sorted(newdict.keys()):
        if val > 30:
            for i in range(len(newdict[val])):
                 magneturl='magnet:?xt=urn:btih:%s'%newdict[val][i]
                 print("magneturl=%s" %magneturl)

if __name__ =="__main__":
    rank()

