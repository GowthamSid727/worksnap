from dotenv import load_dotenv
import os
import requests


# Load environment variables from .env file
load_dotenv()

# Access environment variables
api_key = os.getenv('ACCESS_TOKEN')


url = 'https://api.worksnaps.com:443/api/projects'

# Set the request headers
headers = {'Authorization': 'Token ' + api_key}

# Make the API request
response = requests.get(url, headers=headers)

# Print the response
print(response.json())