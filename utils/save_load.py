import json
import os

DATA_PATH = "data/routes.json"

def load_routes():
    if not os.path.exists(DATA_PATH):
        return {}
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_routes(routes_dict):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(routes_dict, f, ensure_ascii=False, indent=2)

def add_route_for_date(date_str, place_items):
    routes = load_routes()
    routes[date_str] = place_items
    save_routes(routes)

def get_places_by_date(date_str):
    routes = load_routes()
    return routes.get(date_str, [])