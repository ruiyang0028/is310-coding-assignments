import requests
import json
import os

# LOTR MediaWiki API
LOTR_URL = "https://lotr.fandom.com/api.php"

# Metropolitan Museum of Art API
MET_URL = "https://collectionapi.metmuseum.org/public/collection/v1"


def get_lotr_data():
    params = {
        "action": "query",
        "list": "search",
        "srsearch": "Gandalf",
        "format": "json"
    }

    response = requests.get(LOTR_URL, params=params)

    if response.status_code != 200:
        print("LOTR API error:", response.status_code)
        return None

    data = response.json()

    print("\nLOTR API Response:")
    print(json.dumps(data, indent=4))

    return data


def get_met_data():
    params = {
        "q": "Vincent van Gogh",
        "hasImages": True
    }

    response = requests.get(
        f"{MET_URL}/search",
        params=params
    )

    if response.status_code != 200:
        print("Met API error:", response.status_code)
        return None

    data = response.json()

    print("\nMet Museum API Response:")
    print(json.dumps(data, indent=4))

    return data


def save_data(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"Saved data to {filename}")


if __name__ == "__main__":
    lotr_data = get_lotr_data()
    met_data = get_met_data()

    if lotr_data is not None:
        save_data(lotr_data, "lotr_data.json")

    if met_data is not None:
        save_data(met_data, "met_data.json")
