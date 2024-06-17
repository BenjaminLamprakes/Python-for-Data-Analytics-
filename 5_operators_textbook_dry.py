#3 types of operators (textbook stuff)

#Arithmetic, Assigment, and Comparison operators. 

#Arithmetic operators  
#1) basic (+,-, *, /)  
#--------------------- strings to do not have a subtract method. Print("whats up " - "up") does not work. "What's ".__add__("up?") 
#2)  % (remainder) 5%2 = 1 
#3)  ** (exponent) 3**2 = 9 
#4) // devision that results in an integer, not a float. 5//3 == 1, 7//3 == 2 and so on 



#Assignment operators and why I will always just make variables. 
#1)  = is assigning a variable like x = 5 
#1.1) == is comparing a value, if they are equal, its true, if not, its false. 5==5 is true, 5==4 is false but 5=4 means you assign 5 to be 4 
#2) x -= 3  means x = x - 3 which will result in x = 2 
#3) x += 3 result is 8 
#etc. 

#real life example  of x -= 3 
#option 1 using the method 
stock_count = 100
items_sold = 30
stock_count -= items_sold
print(f"Remaining stock count: {stock_count}")


#option 2  - my prefered way, calculates the result separately and stores it in remaining_stock_count, which can be useful if you need to reuse or manipulate the result further in your code.
stock_count = 100
items_sold = 30
remaining_stock_count = stock_count - items_sold
print(f"Remaining stock count: {remaining_stock_count}")


#- comparison is just ==, !=, <, >, <=, >= 