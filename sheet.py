#
#Google API sheet logic
#

def authorize():
	###You need 'credentials.json' file from Google API inside folder
	creds = None
	SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
	# The file token.pickle stores the user's access and refresh tokens, and is
	# created automatically when the authorization flow completes for the first
	# time.
	if os.path.exists('token.pickle'):
		with open('token.pickle', 'rb') as token:
			creds = pickle.load(token)
		# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
	else:
		flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
	creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
	with open('token.pickle', 'wb') as token:
		pickle.dump(creds, token)
	service = build('sheets', 'v4', credentials=creds)
	print("Login succesfull")
	return sheet = service.spreadsheets()

def read_range(sheet,sheet_range,spreadsheet_id):
	result = sheet.values().get(spreadsheetId=spreadsheet_id,range=sheet_range).execute()
	return values = result.get('values', [])

def write(sheet,sheet_cell,spreadsheet_id, value):
	values = [[str(value)]]
	body = {'values':values}
	result = sheet.values().update(spreadsheedId=spreadsheet_id, range=sheet_cell, valueInputOption='RAW', body=body).execute()
	print(value+" value was written to "+sheet_cell+" cell")
