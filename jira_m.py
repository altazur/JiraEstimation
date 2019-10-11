from jira import JIRA
import traceback

def login(url, login_name, login_pwd):
	try:
		jira = JIRA(options={'server':url}, basic_auth=(login_name, login_pwd))
	except ConnectionError:
		jira = None
		print("ConnectionError")
	print("Login succesfull")
	return jira

#Return a generator
def get_dev_estimate_precision(url, login_name, login_pwd, developer_names_list):
	#Get project from the login method
	jiraAPI =  login(url, login_name, login_pwd)
	fot_project = jiraAPI.project('FOT')
	fot_project_id = fot_project.id
	#Get last release id from the porject
	last_release_id = fot_project.raw['versions'][len(fot_project.raw['versions'])-1]['id']
	#Search returns 50 items. maxResult arg can exceed it. For now we don't use maxResult cuz 50 is more than enough
	developer_precision={}
	for developer_name in developer_names_list:
		original_estimate_sum = 0
		timespent_sum = 0
		try:
			developer_issues = jiraAPI.search_issues("project ="+fot_project_id+" AND fixVersion="+last_release_id+" AND assignee='"+developer_name+"'")
		except NameError:
			tb = traceback.format_exc()
			print("Project, release or name are not found")
			break
		for issue in developer_issues:
			original_estimate_sum += issue.fields.timeoriginalestimate or 0
			timespent_sum += issue.fields.timespent or 0
		try:
			yield (timespent_sum/original_estimate_sum if (timespent_sum is not 0 and original_estimate_sum is not 0) else 0, developer_name)
		except ZeroDivisionError:
			tb = traceback.format_exc()
			return 0
	
