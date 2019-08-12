from jira import JIRA

#Init
original_estimate_sum = 0
timespent_sum = 0
estimation_percision_coef = 0

login_name = input("Login:" )
login_pwd = input("Password: ")

#Login
jira = JIRA(options={'server':'https://jira.web100.com.ua'}, basic_auth=(login_name, login_pwd))

#Getting the project
fot_project = jira.project('FOT')
#Gettin project_id
fot_project_id = fot_project.id

#Getting the last release id
last_release_id = fot_project.raw['versions'][len(fot_project.raw['versions'])-1]['id']

#Search returns 50 items. maxResult arg can exceed it. For now we don't use maxResult cuz 50 is more than enough
#For protoype we count the specific user Estimation

developer_issues = jira.search_issues("project ="+fot_project_id+" AND fixVersion="+last_release_id+" AND assignee='Yuriy Yefremov'")

for issue in developer_issues:
	original_estimate_sum += issue.fields.timeoriginalestimate
	timespent_sum += issue.fields.timespent

print("Developer timespent sum is: "+str(timespent_sum/60/60)+"hours")
print("Developer estimation sum is: "+str(original_estimate_sum/60/60)+"hours")
estimation_percision_coef=timespent_sum/original_estimate_sum
print("Developet precision is "+str(estimation_percision_coef)+" %")

