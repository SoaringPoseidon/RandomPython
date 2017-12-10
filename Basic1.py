import os

print ("hello world")



f = "abc"
#def main():
 #   print("Hello WOrld")
 #   print (f)
 #   print ("string type " + str(123))

def myFunc():
    global f #This line makes f a global variable
    f = "def"
    print (f)

def main():
    name = input("What is your name?")
    print ("Your name is " + name)

    for i in range(1,10,2):
        print (i," ", sep='|', end='') # end='' supress new line for each print. sep='|' user | as seperator
        #print (i)
    else:
        print ("dont printing") # else for for statement. Only execute if all elements have been iterated. 

def print_dir_contents(dir):
    import os # this is not going to be imported multiple times even if this function is called many times. Because it's cached 
    print ("dir is " + dir)
    for child in os.listdir(dir):
        print(child)
        if os.path.isdir(child):
            print_dir_contents(child)

if __name__ == "__main__":
    print("Called from main")
    #main()
   # prrint_dir_contents(os.path.basename(os.path.dirname(os.path.realpath(__file__))))
    print_dir_contents(os.path.dirname(os.path.realpath(__file__)))
else:
    print("Not called from main")

myFunc()
print (f)

del f # this line deletes variable f. You can delete variable in python
#print (f)

def multi_add(*args):
    result =0
    for i in args:
        result += i
    return result

print(multi_add(3,4,5,6))

x, y = 10, 100


st = "x is greater than y" if (x>y) else "x is less than or equal to y" #NICE
print (st)

for x in range (4, 9):
    print (x)

days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
for i in days[2:10]: #NICE slicing notation is :
    print (i)

#NICE Using emumerate() to get index
for i, d in enumerate(days):
    print (i,d)

