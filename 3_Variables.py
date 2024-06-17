#variable name = value 

base_salary = 100000
#the variable is created soon as you assign a value to it. 

#operations are your cell references 

bonus_rate = 0.1 
total_salary = base_salary * (1+bonus_rate)

#to check if it works use print()
# output should be 110000.00000000001 which is questionable 

formatted_salary = "%.2f" % total_salary # .2f means 2 decimal places, .0f would mean 0 decimal places and so on. 
print( "$ " + (formatted_salary))


#simple variable example. 

job_id = 101
company_name = 'ABC'
job_title = 'Data Analyst'
job_salary = 125000
job_work_from_home = True

print("Job ID:      ", job_id)
print("Company Name:", company_name)
print("Job Title:   ", job_title)
print("Salary:      ", job_salary)
print("WFH:         ", job_work_from_home)

