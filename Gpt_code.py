import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage to scrape
url = 'https://www.linkedin.com/company/100638267/admin/analytics/updates/'

# Send a request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# TODO: Extract the necessary data
# For example, if you're extracting all the text from paragraphs:
data = [p.get_text() for p in soup.find_all('p')]

# Create a DataFrame
df = pd.DataFrame(data, columns=['Extracted Data'])

# Save the DataFrame to an Excel file
excel_filename = 'extracted_data.xlsx'
df.to_excel(excel_filename, index=False)

print(f'Data extracted and saved to {excel_filename}')
