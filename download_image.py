import requests

url = 'https://media.tacdn.com/media/attractions-splice-spp-674x446/12/3f/38/32.jpg'

response = requests.get(url)

with open('fuji.jpg', 'wb') as file:
    file.write(response.content)
