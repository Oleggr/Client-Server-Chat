import requests 
  

url = 'http://127.0.0.1:8080/'
  
params = {'token': 'bbb'} 

path = input('input path: ')

r = requests.get(url = url + path, params = params) 
  
# data = r.json() 

print(r.text)