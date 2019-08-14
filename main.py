from jira import JIRA
import traceback

#Method return the precision of estimation of given project and release
def get_dev_estimate_precision(project_id, last_release_id, developer_name):
	original_estimate_sum = 0
	timespent_sum=0
	#Search returns 50 items. maxResult arg can exceed it. For now we don't use maxResult cuz 50 is more than enough
	developer_issues = jira.search_issues("project ="+fot_project_id+" AND fixVersion="+last_release_id+" AND assignee='"+developer_name+"'")
	for issue in developer_issues:
		original_estimate_sum += issue.fields.timeoriginalestimate or 0
		timespent_sum += issue.fields.timespent or 0
	try:
		return timespent_sum/original_estimate_sum
	except ZeroDivisionError:
		tb = traceback.format_exc()
		return 0

login_name = input("JIRA login:" )
login_pwd = input("JIRA password: ")
###
### Main flow
###
#Login
try:
	jira = JIRA(options={'server':'https://jira.web100.com.ua'}, basic_auth=(login_name, login_pwd))
except ConnectionError:
	print("ConnectionError")

print("Login succesfull")

#Getting the project
fot_project = jira.project('FOT')
#Gettin project_id
fot_project_id = fot_project.id
#Getting the last release id
last_release_id = fot_project.raw['versions'][len(fot_project.raw['versions'])-1]['id']
#Getting list of developers
developers_list = input("Enter developer name. You also can enter several names separated by comma\n").split(",")
for developer_name in developers_list:
	try:
		print(developer_name+" percision is: "+str(get_dev_estimate_precision(fot_project_id, last_release_id, developer_name)))
	except NameError:
		tb = traceback.format_exc()
		print("Project, release or name are not found")
		break
