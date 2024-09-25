import requests

class GoogleSheets:
    def __init__(self, api_key, sheet_id):
        self.api_key = api_key
        self.sheet_id = sheet_id
        self.base_url = f'https://sheets.googleapis.com/v4/spreadsheets/{self.sheet_id}/values/'

    def fetch_data(self, sheet_name='Sheet1'):
        # Construct the full URL to access the data
        url = f'{self.base_url}{sheet_name}?key={self.api_key}'
        
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parsing the response as JSON
            data = response.json()
            # The data is usually within the 'values' key
            return data.get('values', [])
        else:
            # Handle errors if the request failed
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None

 

#  Google Sheets API key
api_key = 'your api key'

# The ID of  Google Sheet
sheet_id = 'your sheet id'

# Create an instance of GoogleSheets
gs = GoogleSheets(api_key, sheet_id)

# Fetch and print the data from the default sheet (Sheet1)
data = gs.fetch_data()
if data:
    for row in data:
        print(row)


