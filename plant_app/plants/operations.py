import csv

# To add a new Use to a particular plant in the file
def add_use(loaded_plants,plant_name,new_use):
    for plant in loaded_plants:
        if plant["name"].lower() == plant_name.lower():
            plant["uses"].append(new_use)
            return True
    return False

# To add a new plant to the file 
def create_dict(new_name,icount):
    new_dict = {}
    new_dict["name"] = new_name
    new_dict["medicinal"] = True
    new_dict["uses"] = []
    new_dict["image_count"] = icount
    return new_dict

# To view every plants in the file

def view_plants(loaded_plants):
    for pl in loaded_plants:
        print(
            f"Plant: {pl['name']}\n"
            f"Medicinal: {pl['medicinal']}\n"
            f"Uses: {pl['uses']}\n"
            f"Image count: {pl['image_count']}\n"
        )


def export_to_csv(loaded_plants):
    with open("plants.csv","w",encoding="utf-8",newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames = ['name','medicinal','uses','image_count']
        )
        writer.writeheader()
        for p in loaded_plants:
            writer.writerow(p)