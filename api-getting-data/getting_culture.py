import requests
import json

# Met Museum API
BASE_URL = "https://collectionapi.metmuseum.org/public/collection/v1"

def get_met_artworks():
    url = f"{BASE_URL}/search"
    params = {
        "q": "painting",
        "hasImages": True
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Error:", response.status_code)
        return None

    data = response.json()
    print(json.dumps(data, indent=4))

    return data


if __name__ == "__main__":
    get_met_artworks()

