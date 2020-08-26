from jira_m import get_dev_estimate_precision
from sheet import authorize, write
import argparse

def main(jiraURL, jiraLoginName, jiraPwd, developerNames, sheetId, project_code):
	try:
		developers_names = developerNames.split(",")
	except AttributeError:
		print("Wrong arguments. Try --help for help")	
		quit()
	print(developers_names)
	sheet = authorize()
	precision_name_gener = get_dev_estimate_precision(jiraURL, jiraLoginName, jiraPwd, developers_names, project_code)
	if sheetId is None:
        	for i in precision_name_gener:
                     print ("\n"+str(i[0]).replace('.', ',')+str(i[1]))
	else:
		[write(sheet, sheetId, dev_prec[0], dev_prec[1]) for dev_prec in precision_name_gener]

if __name__=="__main__":
	parser = argparse.ArgumentParser(description="Takes the developer estimation precision from given jira url and writes it to the given GoogleSheet")
	parser.add_argument("--jiraURL", type=str)
	parser.add_argument("--developerNames", type=str)
	parser.add_argument("--sheetId", type=str)
	parser.add_argument("--jiraLoginName", type=str)
	parser.add_argument("--jiraPwd", type=str)
    pareser.add_argument("--projectCode", type=str)
	args = parser.parse_args()
	#Call main method with all arguments
	main(args.jiraURL, args.jiraLoginName, args.jiraPwd, args.developerNames, args.sheetId, args.projectCode)
