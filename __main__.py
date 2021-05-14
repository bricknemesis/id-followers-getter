
import requests

def getList(url):
    response = requests.get(url)
    data = response.json()
    return data

def main():
    id = int(input("Please enter the user ID whose followers you wish to view: "))
    url = f"https://friends.roblox.com/v1/users/{id}/followings?sortOrder=Desc&limit=100"

    data = getList(url)
    dataDicts = [data]
    while data.get("nextPageCursor"):
        vurl = url + "&cursor=" + data["nextPageCursor"]
        data = getList(vurl)
        dataDicts.append(data)
    
    nameCache = {}
    sum = 0
    for dc in dataDicts:
        for data in dc["data"]:
            if nameCache.get(data["name"]): continue
            print(data["name"])
            nameCache[data["name"]] = True
            sum += 1
    
    print(f"\nGathered a total of {sum} {(sum == 1 and 'follower' or 'followers')} for ID {id}")


if __name__ == "__main__":
    while True:
        main()