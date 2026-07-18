import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "login_data.json"


def load_login_data():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)["users"]