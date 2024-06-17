


#for example 

# if you scrape 1000 job postings and you want to filter the results to only show a skills that have at least 75% of your skills mentioned. 
#found the best way to do it is to just add 1 condition at a time, make sure it works and then add it on to the main code, you can add as many elif statements you want. 

# Step 1: Create a library of your skills
my_skills = ['Python', 'Data Analysis', 'Machine Learning', 'SQL', 'Problem Solving']

# Sample job postings
job_postings = [
    {'company': 'Company A', 'skills': ['Cooking Dinner', 'Washing Dishes Learning', 'SQL']},
    {'company': 'Company B', 'skills': ['Python', 'Data Analysis', 'Problem creator']},
    {'company': 'Company C', 'skills': ['Python', 'Data Analysis', 'creator', 'SQL']},
    {'company': 'Company D', 'skills': ['Data Analysis', 'entertaining', 'Problem Solving']}
]  # Added the closing bracket here

# Matching algorithm
def calculate_skill_match(my_skills, job_skills):
    # Calculate intersection of skills
    common_skills = set(my_skills) & set(job_skills)
    # Calculate match percentage
    match_percentage = len(common_skills) / len(job_skills) * 100
    return match_percentage

# Filter job postings
required_match_percentage = 50 #edit this for whatever treshhold you like 

matched_jobs = []
for job in job_postings:
    match_percentage = calculate_skill_match(my_skills, job['skills'])
    if match_percentage >= required_match_percentage:
        matched_jobs.append((job['company'], match_percentage))

# Print matched job postings
for company, percentage in matched_jobs:
    print(f"Company: {company}, Match Percentage: {percentage}%")



#now if you'd include years of experience ... 

# Step 1: Create a library of your skills
my_skills = ['Python', 'Data Analysis', 'Machine Learning', 'SQL', 'Problem Solving']

# Sample job postings including years of experience
job_postings = [
    {'company': 'Company A', 'skills': ['Python', 'Machine Learning', 'SQL'], 'experience_years': 3},
    {'company': 'Company B', 'skills': ['Python', 'Data Analysis', 'Problem Solving'], 'experience_years': 2},
    {'company': 'Company C', 'skills': ['Python', 'Data Analysis', 'Machine Learning', 'SQL'], 'experience_years': 5},
    {'company': 'Company D', 'skills': ['Data Analysis', 'SQL', 'Problem Solving'], 'experience_years': 4}
]

# Matching algorithm
def calculate_skill_match(my_skills, job_skills):
    # Calculate intersection of skills
    common_skills = set(my_skills) & set(job_skills)
    # Calculate match percentage
    match_percentage = len(common_skills) / len(job_skills) * 100
    return match_percentage

# Filter job postings
required_match_percentage = 75
required_experience_years = 3

matched_jobs = []
for job in job_postings:
    match_percentage = calculate_skill_match(my_skills, job['skills'])
    if match_percentage >= required_match_percentage and job['experience_years'] >= required_experience_years:
        matched_jobs.append((job['company'], match_percentage, job['experience_years']))
    elif match_percentage >= required_match_percentage:
        print(f"Company {job['company']} requires more experience.")
    else:
        print(f"Company {job['company']} does not meet skill requirements.")

# Print matched job postings
for company, percentage, years_experience in matched_jobs:
    print(f"Company: {company}, Match Percentage: {percentage}%, Years of Experience: {years_experience}")

