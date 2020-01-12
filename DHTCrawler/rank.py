import json
import operator

def rank():
    jsonObj = open("DHTCrawler/pretty.json")

    dictObj = json.load(jsonObj)

    newdict = {}

    for movie, val in dictObj.items():
        newdict.setdefault(val,[]).append(movie)


    for val in sorted(newdict.keys()):
#    print("in for")
        if val > 2:
            print(val, newdict[val])
#        print("in if")

if __name__ == "__main__":
    rank()
