import requests
from send_email import send_email

api_key = '1551997252ec4f1394ee4da6fdb44c59'

url = ('https://newsapi.org/v2/everything?'
       'q=tesla&from=2024-05-24&sortBy=publishedAt&'
       'apiKey=1551997252ec4f1394ee4da6fdb44c59')

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
body = ''
# Access the article titles and description
for article in content['articles']:
    if article['title'] is not None and article['description'] is not None:
        body = body + article['title'].upper() + '\n' + article['description'] + 2*'\n'
body.encode('utf-8')
send_email(message=body)