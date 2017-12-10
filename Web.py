from urllib.request import urlopen
from urllib.request import Request
#from urllib.error import HTTPError
import urllib

def printGoogle():
    #gooelUrl = urlopen("https://www.amazon.com/Baume-Mercier-Classima-Executives-Automatic/dp/B00KBCHYSI")
    googleUrl = urlopen("http://www.google.com")
    print ("result code " + str(gooelUrl.getcode()))
    print (gooelUrl)
    data = gooelUrl.read()
    print ("Printing data")
    print (data)

def printAmazon():
    #gooelUrl = urlopen("https://www.amazon.com/Baume-Mercier-Classima-Executives-Automatic/dp/B00KBCHYSI")

    req= Request("https://www.amazon.com/Baume-Mercier-Classima-Executives-Automatic/dp/B00KBCHYSI")

    try:
        amzn = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print (str(e.code))
        print (e.reason)
       #S return

    
   # print ("result code" + str(amzn.read()))




if __name__ == "__main__":
    printAmazon()
