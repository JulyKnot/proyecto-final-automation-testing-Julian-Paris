import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_posts():

    response = requests.get(f"{BASE_URL}/posts")

    assert response.status_code == 200
    assert len(response.json()) > 0

    print("GET ejecutado correctamente.")


def test_create_post():

    payload = {
        "title": "QA Automation",
        "body": "Proyecto Final",
        "userId": 1
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload
    )

    assert response.status_code == 201

    print("POST ejecutado correctamente.")


def test_delete_post():

    response = requests.delete(f"{BASE_URL}/posts/1")

    assert response.status_code == 200

    print("DELETE ejecutado correctamente.")