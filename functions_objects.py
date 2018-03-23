
# functions can be assigned to other object
def first(msg):
    print(msg)    

#first("Hello")

second = first
#second("Hello")

# function can take other functions as arguments
def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(func, x):
    result = func(x)
    return result

print(operate(inc,3))
print(operate(dec,3))

# function can return another function 
def hello_world(h):
      def world(w):
              print(h, w)
      return world # returning function

h = hello_world # assigning
x = h("hello") # assigning

(x("world"))

# storing functions in a list
function_list = [h, x]
print(function_list)