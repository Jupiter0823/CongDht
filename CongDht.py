import argparse 
import json
import operator
from DHTCrawler.downloader import download
from DHTCrawler.rank import rank 
def process_command():
    parser = argparse.ArgumentParser(description="Start CongDht with flag")
    parser.add_argument("-d", action="store_true", help="Start download with arguments")
    parser.add_argument("-r", action="store_true", help="Show rank of Crawler")
    parser.add_argument("-a", action="store_true", help="List out all hash info from crawler")
    return parser


def command_line():
    parser=process_command()
    args=vars(parser.parse_args())

    if args["d"]:
        download()
    if args["r"]:
        rank()
    if args["a"]:
        jsonObj=open('DHTCrawler/result.json')
        dictObj=json.load(jsonObj)
        print(dictObj)

if __name__ == "__main__":
    command_line()





    
