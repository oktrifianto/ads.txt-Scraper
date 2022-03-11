import requests

def getAdsTXT():
  print("Please input your url : ")
  url = input()
  x   = f'https://{url}/ads.txt'
  r   = requests.get(x)
  return r.text # return ads.txt

print(getAdsTXT())