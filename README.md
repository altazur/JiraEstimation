Python script to obtain developers' estimation precision

!Need credentials.json from your Google Sheet API aplication inside the project folder

Usage:
1. Help: main.py --help
2. Console output (without unnecesary --sheetId arg): main.py --jiraURL https://example.com --developerName 'Goerge Doe,Jim Doe'  --jiraLoginName your.login --jiraPwd passwords
3. Write to specific Google sheet (where lines are developers and columns are sprints): main.py --jiraURL https://example.com --developerName 'Goerge Doe,Jim Doe' --sheetId 1121EXAMPLE1231 --jiraLoginName your.login --jiraPwd passwords

![dependencies-all](https://img.shields.io/badge/dependencies-jira--2.0.0%20google--api--python--client--1.7.11%20google--auth--1.6.3%20google--auth--httplib2--0.0.3%20google--auth--oauthlib--0.4.0-brightgreen.svg)
