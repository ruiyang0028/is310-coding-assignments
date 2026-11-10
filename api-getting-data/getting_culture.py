
import requests
import json
import os

# ==========================================
# LOTR MediaWiki API
# ==========================================

LOTR_URL = "https://lotr.fandom.com/api.php"


def get_lotr_data():
    print("\nGetting LOTR data...")

    params = {
        "action": "query",
        "list": "search",
        "srsearch": "Gandalf",
        "format": "json"
    }

    try:
        response = requests.get(
            LOTR_URL,
            params=params,
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        print("\nLOTR API Response:")
        print(json.dumps(data, indent=4))

        return data

    except requests.exceptions.RequestException as error:
        print("LOTR API error:", error)
        return None

    except ValueError as error:
        print("LOTR JSON error:", error)
        return None


# ==========================================
# Metropolitan Museum of Art API
# ==========================================

# Search API uses version 1.1
MET_SEARCH_URL = (
    "https://collectionapi.metmuseum.org"
    "/public/collection/v1.1/search"
)

# Object details use version 1
MET_OBJECT_URL = (
    "https://collectionapi.metmuseum.org"
    "/public/collection/v1/objects"
)


def get_met_data():
    print("\nGetting Metropolitan Museum data...")

    # Search for paintings with images
    params = {
        "q": "painting",
        "hasImages": True,
        "limit": 5
    }

    try:
        # Step 1: Search the collection
        response = requests.get(
            MET_SEARCH_URL,
            params=params,
            timeout=20
        )

        response.raise_for_status()

        search_data = response.json()

        object_ids = search_data.get("objectIDs") or []

        print("\nMet Museum Search Results:")
        print(json.dumps(search_data, indent=4))

        if not object_ids:
            print("No paintings with images were found.")
            return None

        # Step 2: Retrieve details for valid object IDs
        paintings = []

        for object_id in object_ids[:5]:

            print(f"\nGetting object {object_id}...")

            object_url = f"{MET_OBJECT_URL}/{object_id}"

            try:
                object_response = requests.get(
                    object_url,
                    timeout=20
                )

                object_response.raise_for_status()

                object_data = object_response.json()

                # Save selected information
                painting = {
                    "objectID": object_data.get("objectID"),
                    "title": object_data.get("title"),
                    "artist": object_data.get("artistDisplay"),
                    "date": object_data.get("objectDate"),
                    "medium": object_data.get("medium"),
                    "department": object_data.get("department"),
                    "culture": object_data.get("culture"),
                    "country": object_data.get("country"),
                    "primaryImage": object_data.get("primaryImage"),
                }

                paintings.append(painting)

                print("Retrieved:", painting["title"])

            except requests.exceptions.RequestException as error:
                print(
                    f"Could not retrieve object {object_id}:",
                    error
                )

                continue

        if not paintings:
            print("No painting details could be retrieved.")
            return None

        data = {
            "total": search_data.get("total", 0),
            "search_query": "painting",
            "paintings": paintings
        }

        print("\nMet Museum Data:")
        print(json.dumps(data, indent=4, ensure_ascii=False))

        return data

    except requests.exceptions.RequestException as error:
        print("Met Museum API error:", error)
        return None

    except ValueError as error:
        print("Met Museum JSON error:", error)
        return None


# ==========================================
# Save Data
# ==========================================

def save_data(data, filename):

    if data is None:
        print(f"No data to save for {filename}")
        return

    try:
        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print(f"Saved data to {filename}")

    except OSError as error:
        print(f"Error saving {filename}:", error)


# ==========================================
# Main Program
# ==========================================

if __name__ == "__main__":

    print("=" * 50)
    print("API DATA COLLECTION")
    print("=" * 50)

    # Get LOTR data
    lotr_data = get_lotr_data()

    # Get Met Museum data
    met_data = get_met_data()

    # Save LOTR data
    if lotr_data is not None:
        save_data(
            lotr_data,
            "lotr_data.json"
        )

    # Save Met Museum data
    if met_data is not None:
        save_data(
            met_data,
            "met_data.json"
        )

    print("\n" + "=" * 50)
    print("PROGRAM FINISHED")
    print("=" * 50)
