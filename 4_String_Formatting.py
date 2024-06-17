#"This is a string in double quotes"
#'This is a string in single quotes'
#help(str) for the documentation 

#combining strings using +
 
# 'string' + (variable) 
#step 1 #creating the variable 
role = 'Data Analyst'
skill = 'Python' 

#step 2 call variables (without function) 
print(role + ' ' + skill) #' ' is used to create a space 

#str.format()
#The str.format() method uses curly braces {} as placeholders. It's more flexible than %-formatting and allows for reordering and reuse of arguments.

print('Role: {}, Skill required: {}'.format(role, skill) )  #this gives you a lot more flexibility and overall just a better method.


#Using join()
random_numbers_I_want_to_seperate_with_commas_xD_I_realize_this_is_way_too_long_but_its_been_13_hours_and_my_brain_is_done  = "123485244"
print(', '.join(random_numbers_I_want_to_seperate_with_commas_xD_I_realize_this_is_way_too_long_but_its_been_13_hours_and_my_brain_is_done))

skills = ['Python', 'SQL']
print('Role: ' + role + ', Skills required: ' + ', '.join(skills)) #more common use of join 





