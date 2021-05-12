import requests
import json
import sqlite3
response = requests.get('http://api.citybik.es/v2/networks')
print(response.text)
print(response.headers)
print(response.status_code)
response2 = response.json()


with open('N.json','w') as N:
    json.dump(response2,N,indent=4)



for each in response2["networks"]:
    print(each["location"]["city"])
    print(each["company"][0]+", "+each["location"]["country"])



bike = sqlite3.connect("bike.sqlite")
c = bike.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS bicycle
         (id INTEGER PRIMARY KEY AUTOINCREMENT,
         company VARCHAR(255),
         country VARCHAR(50))
''')

info = []

try:

    for x in response2["networks"]:
        print(x)
        country = x["location"]["country"]
        company = x["company"][0]
        line = [company, country]
        info.append(line)
except:
    print('none')


c.executemany('''INSERT INTO bicycle(company,country)
             VALUES(?,?)
''',info)


bike.commit()
bike.close()








print(json.dumps(response2,indent=4))