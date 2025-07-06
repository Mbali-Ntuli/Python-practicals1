#Loop Control  Statements

fruits = ["apple","banana","cherry","orange"]

for fruit in fruits:
    if fruit== "cherry":
        break #Exits loop if cherry is found
    print(fruit)
    
    print()
        
for fruit in fruits:
    if fruit== "cherry":
        continue #Skips cherry and moves to iteration
    print(fruit)
    
    print()
    
    for fruit in fruits:
     if fruit== "cherry":
        pass #placeholder, no action needed for cherry
    print(fruit)
    
    
    