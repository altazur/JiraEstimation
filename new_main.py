from jira_m import get_dev_estimate_precision
from sheet import authorize, write
import argparse

def main(jiraURL, jiraLoginName, jiraPwd, developerNames, sheetId):
	developers_names = developerNames.split(",")
	sheet = authorize()
	if sheetId is None:
		print ("\n"+get_dev_estimate_precision(jiraURL, jiraLoginName, jiraPwd, developers_names))
	else:
		

if __name__=="__main__":
	parser = argparse.ArgumentParser(description="Takes the developer estimation precision from given jira url and writes it to the given GoogleSheet")
	parser.add_argument("--jiraURL", type=str)
	parser.add_argument("--developerNames", type=str)
	parser.add_argument("--sheetId", type=str)
	parser.add_argument("--jiraLoginName", type=str)
	parser.add_argument("--jiraPwd", type=str)
	args = parser.parse_args()
	#Call main method with all arguments
	main(args.jiraURL, args.jiraLoginName, args.jiraPwd, args.developerNames, args.sheetId)
