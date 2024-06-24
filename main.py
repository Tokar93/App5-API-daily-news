import requests

api_key = '1551997252ec4f1394ee4da6fdb44c59'

url = ('https://newsapi.org/v2/everything?'
       'q=tesla&from=2024-05-24&sortBy=publishedAt&'
       'apiKey=1551997252ec4f1394ee4da6fdb44c59')

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content['articles']:
       print(article['title'])