#Decorators
#Decorators are a way to dynamically alter the functionality of your functions. So for example, if you wanted to log information when a function is run, you could use a decorator to add this functionality without modifying the source code of your original function.
#my own word: Decotator is wrapper(function or class) around wrapper of a function. 
#decorators can be chained. But we need to use @wrapper deco for the inner (wrapper) function. 

from functools import wraps #allow chained decorators

def outer_function(msg):
    def innter_function():
        print (msg)
    return innter_function

def closure_example():
    #this is closure example
    my_func = outer_function("Hi")
    my_func2 = outer_function("Bye")

    my_func()
    my_func2()

def decorator_function(original_function):

    @wraps(original_function) #allow chained decorators
    def wrapper_function(*args, **kwargs): #Pass arguments to original_function below
        print("wrapper called before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

def display():
    print('display func is called')

def decorator_example():
    decorated_display = decorator_function(display) # same as adding @decorator_fucntion on display
    decorated_display()

    show()
    display_info("sean", 21)
    display_info2("sean", 21)
    display_info3("sean", 21)
    display_info4("sean", 21)
    display_info5("sean", 21)

@decorator_function
def show():
    print('show func is called')

@decorator_function
def display_info(name, age):
    print('display info is called with arguments {},{}'.format(name,age))

#use class as decorator instead of function. below is an class example
class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function #tie original_function with the instance of this class

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@decorator_class #decotrator using class
def display_info2(name, age):
    print('display info is called with arguments {},{}'.format(name,age))

def my_logger(orig_func):
    import logging #this will be imported only once even if my_logger is called many times. Python cached the lib.
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__),level=logging.INFO)

    @wraps(orig_func) #allow chained decorators
    def wrapper(*args,**kwargs):
        logging.info('Ran with args:{} and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper

@my_logger
def display_info3(name,age):
    print ('display info3 called for {} who is {}yo'.format(name, age))

def my_timer(orig_func):
    import time

    @wraps(orig_func) #allow chained decorators
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print("{} run in : {} sec".format(orig_func.__name__, t2))
        return result
    return wrapper

@my_timer
def display_info4(name,age):
    import time
    print ('display info4 called for {} who is {}yo'.format(name, age))
    time.sleep(1)

#chain decotrators together
@my_logger
@my_timer
def display_info5(name,age):
    print ('display info5 called for {} who is {}yo'.format(name, age))

#this is the same as below
#display_info5 = my_logger(my_timer(display_info5))
if __name__ == "__main__":
    closure_example()
    decorator_example()