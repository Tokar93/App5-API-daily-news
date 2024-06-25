import requests, os
from send_email import send_email

topic = 'tesla'
#api_key = os.getenv((API_KEY))
url = ("https://newsapi.org/v2/everything?"
       "q=tesla&"
       "from=2024-05-25&"
       "sortBy=publishedAt&"
       "apiKey=1551997252ec4f1394ee4da6fdb44c59&"
       "language=en")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
body = ""
# Access the article titles and description
for article in content['articles'][:20]:
    if article['title'] is not None and article['description'] is not None and 'Removed' not in article['title']:
        body = (body + article['title'].upper() + '\n'
                + article['description']
                + '\n' + article['url'] + 2*'\n')
body = 'Subject: News for today!\n' + body
new_body = body.encode("utf-8")
send_email(message=new_body)