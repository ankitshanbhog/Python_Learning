import json
from pathlib import Path

def load_plants():
    file_path = (Path(__file__).parent.parent) / "plants.json"
    with open(file_path , "r",encoding="utf-8") as file:
        loaded_plants = json.load(file)
    return loaded_plants

def save_plants(plants):
    file_path = (Path(__file__).parent.parent) / "plants.json"
    with open(file_path , "w",encoding="utf-8") as file:
        json.dump(plants,file,indent=4)
        

