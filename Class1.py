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

def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i);
    return result

def square_numbers_gen(nums):
    for i in nums:
        yield (i*i)

def test_generator():
    nums=[1,2,3,4,5,6]
    print (square_numbers(nums))

    nums_gen = square_numbers_gen(nums)
    print (next(nums_gen))
    print (next(nums_gen))
    print (next(nums_gen))
    print (next(nums_gen))
    print (next(nums_gen))

    nums_gen2 = square_numbers_gen(nums)
    for i in nums_gen2:
        print(i)


if ( __name__ == "__main__"):
#    main()
    test_generator()
 