class myClass():
    def method1(self):
        print ( "myCLass method1")

    def method2(self, somestr):
        print ("myCLass method2 ", somestr)

def main():
    c = myClass();
   
    c.method1()
    c.method2("arg2")

    f = open("c:/users/sean/documents/text.txt", "w+")

    for i in range(10):
        f.write("this is line %d\r\n" % i)
    f.close()

    f1 = open("c:/users/sean/documents/text.txt","a+")

    for j in range(5,10,2):
        f1.write("this is new line %d\r\n" % j)
    f1.close()

    f2 =  open("c:/users/sean/documents/text.txt","r")
  #  if f2.mode == "r":
  #      contents = f2.read()
  #     print (contents)
    fl=f2.readlines()
    for x in fl:
        print (x)

if ( __name__ == "__main__"):
    main()
 