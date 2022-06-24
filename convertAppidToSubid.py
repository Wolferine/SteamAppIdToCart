import time
import traceback
import requests

appIds = []


ids = []
try:

    with open('in.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            lineData = line.split(',')
            for i in lineData:
                i.strip()
                appIds.append(i)

    print("done importing appIds")

    f = open('out.txt', 'w')
    count = 0
    failStreak = 0
    size = len(appIds)
    while count < size:
        appId = appIds[count]
        count += 1

        if failStreak > 5:
            print("To many fails. Sleeping for 1 minute.")
            print(ids)
            f.flush()
            time.sleep(60)
            count -= failStreak
            failStreak = 0
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

        if app['success'] is False:
            failStreak += 1
            print("failed to get data from json. Skipping.")
            continue
        data = app["data"]
        if data is None:
            failStreak += 1
            print("data not found. Skiping.")
            print(app)
            continue

        if not("packages" in data):
            failStreak += 1
            print("no packages found. Skipping.")
            continue
        pck = data["packages"]
        if pck is None:
            failStreak += 1
            print("no packages found. Skipping.")
            print(data)
            continue


        if len(pck) > 1:
            print("multiple packages found for appId: " + appId + ", adding only first. " + pck.__str__())
        else:
            print("added")
        f.write(str(pck[0]) + "," + "\n")
        f.flush()
        ids.append(pck[0])
        failStreak = 0
    print(ids)
    
except:
    traceback.print_exc()
    print("Early termination")
    print(ids)

finally:
    f.close()
print("done")
input("Press Enter to close.")