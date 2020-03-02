x = 15
def change(): 
  
    # using a global keyword 
    global x 
  
    # increment value of a by 5 
    x = x + 5 
    print("Value of x inside a function :", x) 
change() 
print("Value of x outside a function :", x) 