import time
import requests

appIds = []

ids = []
try:
    count = 0
    failStreak = 0
    size = len(appIds)
    while count < size:
        appId = appIds[count]
        
        count += 1
        if failStreak > 10:
            print("To many fails. Sleeping for 5 minutes.")
            print(ids)
            time.sleep(300)
            count - 10
            continue
            
        print("sending request for appId: " + appId)
        r = requests.get(f"https://store.steampowered.com/api/appdetails?appids={appId}")
        jsontemp = r.json()
        if jsontemp is None:
            failStreak += 1
            print("appId not found, no data returned. Skipping.")
            continue
        app = jsontemp[appId]
        if app is None:
            failStreak += 1
            print("appId not in json. Skipping.")
            print(jsontemp)
            continue
        data = app["data"]
        if data is None:
            failStreak += 1
            print("data not found. Skiping.")
            print(app)
            continue
        pck = data["packages"]
        if pck is None:
            failStreak += 1
            print("packages not found. Skipping.")
            print(data)
            continue
        if len(pck) > 1:
            print("multiple packages found for appId: " + appId + ", adding only first. " + pck.__str__())

        ids.append(pck[0])
        failStreak = 0
        
    print(ids)
    

except:
    print("Early termination")
    print(ids)