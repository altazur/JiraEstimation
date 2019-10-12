#
#Google API sheet logic
#
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def authorize():
	###You need 'credentials.json' file from Google API inside folder
	creds = None
	SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
	# The file token.pickle stores the user's access and refresh tokens, and is
	# created automatically when the authorization flow completes for the first
	# time.
	if os.path.exists('token.pickle'):
		print("Token exists")
		with open('token.pickle', 'rb') as token:
			creds = pickle.load(token)
		# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			print("refreshing credentials")
			creds.refresh(Request())
		else:
			print("Creating new token")
			flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
			creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
		with open('token.pickle', 'wb') as token:
			pickle.dump(creds, token)
	service = build('sheets', 'v4', credentials=creds)
	print("Google login succesfull")
	return service.spreadsheets()

def read_range(sheet,sheet_range,spreadsheet_id):
	result = sheet.values().get(spreadsheetId=spreadsheet_id,range=sheet_range).execute()
	return result.get('values', [])

def write(sheet,spreadsheet_id, dev_precision, dev_name): 
	values = [[str(dev_precision).replace('.', ',')]]
	body = {'values':values}
	m_range = find_last_empy_cell(sheet,spreadsheet_id,dev_name)
	result = sheet.values().update(spreadsheetId=spreadsheet_id, range=m_range, valueInputOption='RAW', body=body).execute()
	print(str(dev_precision)+" value was written to "+m_range+" cell")

def find_last_empy_cell(sheet,spreadsheet_id,developer_name):
	result = sheet.values().get(spreadsheetId=spreadsheet_id,range='A1:Z10').execute()
	#List for characteres association
	cell_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	values = result.get('values', [])
	for cell in values:
		if cell[0] == developer_name:
			#Debug
			print('['+cell_letters[(len(cell))]+':'+str(values.index(cell)+1)+']')
			return str(cell_letters[(len(cell))]+str(values.index(cell)+1))

			break
