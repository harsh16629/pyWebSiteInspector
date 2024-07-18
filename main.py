import requests
import time
import os
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters"



def webWatcher():
    headers = {'Pragma': 'no-cache', 'Cache-Control': 'no-cache'}
    response = requests.get(url, headers=headers)

    if not os.path.exists("changeLog.txt"):
        open('changeLog.txt', 'w+', encoding='utf-8').close()

    with open("changeLog.txt", 'r', encoding='utf-8') as fileHead:
        previousLog = fileHead.read()
    
    currentLog = response.text

    if previousLog == currentLog:
        return False
    
    else:
        with open('changeLog.txt', 'w+', encoding='utf-8') as fileHead1:
            fileHead1.write(currentLog)

       


def main():
    while True:
        if webWatcher():
            print("Change detected!")
        else:
            print("No change detected!")
        time.sleep(11)


if __name__ == '__main__':
    main()
    

    