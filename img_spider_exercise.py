import requests
headers = {'user-agent': 
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/77.0.3865.90 Safari/537.36'
 }
r = requests.get("https://www.qikeman.com/chapter/18583", headers =headers)
print(r.text)
#file_name = 'html.txt'
#with open(file_name, 'w') as file_object:
    #file_object.write(rr)
