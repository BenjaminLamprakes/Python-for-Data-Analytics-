# Define a function to return job skills
def job_skills():
    return ['sql', 'tableau', 'excel', 'dishwasher']  # List of skills

# Print original job_skills list 
print(job_skills())  # Output: ['sql', 'tableau', 'excel', 'dishwasher']

# Good practice: Work with the data without changing the original data (job_skills). Once you change it, remember to use modified_skills_list to print. Not job_skills()
modified_skills_list = job_skills()

# Remove 'excel' from the list and keep 'dishwasher'
modified_skills_list.remove('excel')

# Print the modified list of job skills
print(modified_skills_list)  # Output: ['sql', 'tableau', 'dishwasher']

# If you want the first result of the list, you can 'index' your list (index always starts at 0)
print(modified_skills_list[0])  # Output: 'sql'

# Change 'dishwasher' to 'coding' in modified_skills_list
modified_skills_list[2] = 'coding'  # Output: ['sql', 'tableau', 'coding']

#if you want to add skills to your list at the end of your list 
modified_skills_list.append('social') #Output ['sql', 'tableau', 'coding', 'social']

#if you want to add a skill at a specific place in your list
modified_skills_list.insert(2,'python') #output ['sql', 'tableau', 'python', 'coding', 'social']

#if you have a 2 lists you want to combine 
soft_skills = ['communication']

all_skills = soft_skills + modified_skills_list 
print(all_skills) #output ['communication', 'sql', 'tableau', 'python', 'coding', 'social']

