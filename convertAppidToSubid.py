import requests

#as String array ["appId1","appId2","appId3"]
appIds = ["538920"]

ids = []
for appId in appIds:
    r = requests.get(f"https://store.steampowered.com/api/appdetails?appids={appId}")
    jsontemp = r.json()
    app = jsontemp[appId]
    data = app["data"]
    pck = data["packages"]
    ids.append(pck[0])

print(ids)