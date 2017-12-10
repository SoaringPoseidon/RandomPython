import json
import urllib
import urllib.error
import urllib.request

def printResults(data):
    theJSON = json.loads(data) # json load string

    if "title" in theJSON["metadata"]:
        print (theJSON["metadata"]["title"])
        print (theJSON["metadata"])

##output the number of events, plus the magnitude and each event name
    count = theJSON["metadata"]["count"]
    print(str(count) + "event recorded")
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 3.0:
            print ( "there is an earthquake at " + i["properties"]["place"] 
               + " at mag " + str(i["properties"]["mag"]))

def main():
    try:
       url  = urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson")
    except urllib.error.URLError as e:
        print ("URL error " + e.code + e.strerror)
        return

    print("code is " + str(url.getcode()))

    if (url.getcode() == 200):
        data = url.read()
        printResults(data)

    #print(url.read())

if (__name__ == "__main__"):
    main()