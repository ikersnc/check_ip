import requests

def getIP():
    response = requests.get("https://ipinfo.io/json", verify = True)

    if response.status_code != 200:
        return f'Status: {response.status_code} Algo ha salido mal :('
        exit()

    return response.json()["ip"]

if __name__ == "__main__":
    print(getIP())
