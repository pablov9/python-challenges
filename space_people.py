
import requests #Usar pip install requests en la terminal
response=requests.get("http://api.open-notify.org/astros.json")
json=response.json()
print("Currently, the people in space are:")
for person in json["people"]:
    print(person["name"])
