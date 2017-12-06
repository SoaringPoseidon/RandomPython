

import os
from os import path
import datetime
import time
from datetime import date as dt_dat
from datetime import time as dt_time
from datetime import timedelta as dt_timedelta

import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    print (os.name)
    print ("Item exits:" + str(path.exists("README.md")))
    print ("Item is file :" + str(path.isfile("README.md")))
    print ("Item is dir :" + str(path.isdir("README.md")))
    print ("Item real path :" + str(path.realpath("README.md")))
    print ("Item real path and name :" + str(path.split(path.realpath("README.md"))))
    #path.split returns a list
    for i in path.split(path.realpath("README.md")):
        print (i);

    print ("Modify time is " + str(path.getmtime("README.md")))
    t = time.ctime(path.getmtime("README.md"))
    #Ctime format
    print (t)
    #Date time format
    dt = datetime.datetime.fromtimestamp(path.getmtime("README.md"))
    print (dt)

    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("README.md"))
    print ("It has been " + str(td) + " since the file last modified")
    print ("Or " + str(td.total_seconds()) + "seconds")

def shellutil():
    if path.exists("README.md"):
        src = path.realpath("README.md")
        head, tail = path.split(src)
        print ("head " + head)
        print ("tail " + tail)

        dst = src + ".bak"
        shutil.copy(src,dst)

        #copy over permission, modification time and other info
        #dst2 = src + ".bak2"
        shutil.copystat(src,dst)

        #os.rename(dst, dst+"rename") 

        #shutil.make_archive("archive", "zip", head)
        if not path.exists("testzip.zip"):
            with ZipFile("testzip.zip", "w") as newzip:
                newzip.write("README.md")
                newzip.write("README.md.bak")
                newzip.write("Basic1.py")
        else:
            print ("zip file already created")

if (__name__ == "__main__"):
   # main()
    shellutil()