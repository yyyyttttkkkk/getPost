import requests

url = 'http://35.238.23.14:9000/compare'
myobj = {'image1': 'somevalue', 'image2': 'somevalue'}

x = requests.post(url, json = myobj)

print(x.text)
