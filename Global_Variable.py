X = "Nagpur"            # This is the Global Variable 
def myfunc():
    print("I'm From", X)      # And Here we Called it inside the function..
myfunc()






#If you create a variable with the same name inside a function, this variable will be local,and can only be used inside the function.

X = "Nagpur"
def myfunc():
    X = "Nagpur"
    print("I Like to live in", X)
myfunc()

print("I love", X ,"Very Much")




# If you use the global keyword, the variable belongs to the global scope:

X = "Fantastic"
def myfunc():
    global X
    X = "Awesome"
myfunc()
    
print("Frullato's Strawberry shake are" , X)

