#'if' means first condition check 
#'elif' means subsequent condition check
#else means last condition check 
# using the "and"' or  "or" operator lets you narrow it down even more 


#very simple example 

# Applicant skill
applicant_skill = 'SQL'

# Skill required for job posting 
job_skill = 'SQL'

# Simulating years of experience for demonstration purposes
years_experience = 1

# Initialize result with a default value
result = 'No Skills Match'

# Check if the applicant's skill matches the required skill of the job posting and they meet the experience requirement.
if applicant_skill != job_skill:
    result = 'Skills still needed'
elif applicant_skill == job_skill and years_experience < 2:
    result = 'More experience needed'
else:
    result = 'Experience matches!'

# Print the result
print(result)
