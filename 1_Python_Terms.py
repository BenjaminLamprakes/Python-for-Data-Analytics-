#Terms to know:

#1 Objects 
#2 Variable
#3 Function
#4 Class
#5 Method
#6 Attribute

#if you wonder about anything you can always run the help function to see the documentation. Like help(str), help(class) etc 

# general help - be ready for a wall of text. 
# help(int)
# help(str)
# help(list)

#whenever you import a library you can also call that library with the help() function to see what it can do. 


#Objects are variables that contain data. The Object data can be anything from int, string etc. If you're unsure you can always create this function to check 
#generally a good idea to always print out each section of the code to see what it does. 

def sample_function():
    return "Hello, World!"

def check_type(obj):
    print(f"The type of the object is: {type(obj)}") #f before the opening quotation mark " indicates that this is an f-string = formatted string literal, use it for formatting. 

# or just use this example as a reminder  
check_type(sample_function) #function 
check_type(42) #int  - whole numbers 
check_type("Hello") #str - text values 
check_type(3.14) #float - decimal numbers 
check_type([1, 2, 3]) #list 


#Variables behave the same as cells in an excell spreadsheet. You can store data in it and call back to it. Just like in excell, good use of variables lets you avoid doing redudant work.  

job_title = "Data Analyst"
job_salary = 90000

#method 1 converting job_salary into a string since job_salary value contains an int - less flexibility 
print("Job Title: " + job_title + ", Salary: " + str(job_salary)) #"job title" + Job_title function + ", Salary:" + Job_salary function. instead of using cell references you use (variable_name) to call a variable. 

#method 2 using ".format()" -- this method automatically converts variables to strings at the specific place you call it. 
print("Job Title: {}, Salary: {}".format(job_title, job_salary)) 


#for a list of employees or customers its important to assigne unique IDs for each person so you can dedect  duplicates. Use them as primary key in databases etc. 
#more on that later 

#just like excell, variabels that reference the same objects are ...  the same. 
ben_l_job = job_title
print("Ben is a " + (job_title)) #Ben is a Data Analyst 

#in order to make any of this useful, we'd need functions. The print function is great to see what the output is. 

#level 1 function 
print("Whats up, Data Nerds!")

#level 2 function 
def greet():
    return ("Whats up, Data Nerds!")

#to call a function you always do function_name + open parenthesis, no need to type out print
greet()

#simple way to put it all together (no conditional statements yet, its coming!)
def display_info (title, location, salary): 
     return print(f"JOB:       {title}\nLOCATION:  {location}\nSALARY:    ${salary:,.0f}")

job_title = "Data Analyst"
job_location = "United States"
job_salary = 90000

display_info(job_title, job_location, job_salary)


#Classes are like a template for your records in Excel. It defines the fields that each record will have.

class JobPost:
    def __init__(self, title, location, salary):
        self.title = title
        self.location = location
        self.salary = float(salary)

    def display_info(self):
        return print(f"JOB:       {self.title}\nLOCATION:  {self.location}\nSALARY:    ${self.salary:,.0f}")

#method 1 to print 
job_post = JobPost("Data Analyst", "United States", "90000") #good to see if your class JobPost works but otherwise not very useful 

#method 2 to print 
print(job_post.display_info()) #dont forget () to call the function 

#method 3 to print 
job_info = job_post.display_info() #to shorten it for future use 
print(job_info)

#Attributes:  Attributes are like the columns in your spreadsheet. Each attribute stores specific data for each record or row. 
class JobPost:
    def __init__(self, title, location, salary):
        self.title = title  # Attribute
        self.location = location  # Attribute
        self.salary = salary  # Attribute

#you can imagine having 3 colums in your spreadsheet title, location, salary 