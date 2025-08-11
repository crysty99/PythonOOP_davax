import requests


if __name__ == "__main__":
    # Test pow endpoint
    resp = requests.post(
        "http://127.0.0.1:5000/api/pow",
        json={"base": 2, "exp": 8},
    )
    print("/api/pow:", resp.json())

    # Test fibonacci endpoint
    resp = requests.post(
        "http://127.0.0.1:5000/api/fibonacci",
        json={"n": 10},
    )
    print("/api/fibonacci:", resp.json())

    # Test factorial endpoint
    resp = requests.post(
        "http://127.0.0.1:5000/api/factorial",
        json={"n": 5},
    )
    print("/api/factorial:", resp.json())

    # Test history endpoint
    resp = requests.get("http://127.0.0.1:5000/api/history")
    print("/api/history:", resp.json())
