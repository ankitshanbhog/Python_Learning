import json
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


def load_plants():
    try:
        with open("plants.json","r",encoding="utf-8") as file:
            loadp = json.load(file)
    except FileNotFoundError:
        print("No saved records found. Starting with an empty list.")
        return []
    except json.JSONDecodeError:
        raise 
    else:
        return loadp

try:
    loaded_plants = load_plants()
except json.JSONDecodeError:
    print("Cannot start because the plant data is corrupted.")
    raise SystemExit


while True:
    print("\n======= MediPlant Record Manager ======")
    print("1. View plants")
    print("2. Add a plant")
    print("3. Add a use to a plant")
    print("4. Export plants to CSV")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_plants(loaded_plants)

        
    elif choice == "2":
        new_pl = input("Enter plant name: ").strip()

        if not new_pl:
            print("Plant name cannot be empty.")
            continue

        duplicate = False
        for plant in loaded_plants:
            if plant["name"].strip().lower() == new_pl.lower():
                duplicate = True
                break

        if duplicate:
            print("This plant already exists.")
            continue

        while True:
            try:
                img_c = int(input("Enter the image count for the same: "))

                if img_c < 0:
                    print("Image count cannot be negative.")
                    continue

                break

            except ValueError:
                print("Please enter a valid whole number.")

        new_dict = create_dict(new_pl, img_c)
        loaded_plants.append(new_dict)

        with open("plants.json", "w", encoding="utf-8") as file:
            json.dump(loaded_plants, file, indent=4)

        print("Plant added and saved successfully.")


    elif choice == "3":
        plant_use = input("Enter the plant name: ").strip()

        if not plant_use:
            print("Plant name cannot be empty.")
            continue

        use = input("Enter the new medicinal use: ").strip()

        if not use:
            print("Medicinal use cannot be empty.")
            continue

        found = add_use(loaded_plants, plant_use, use)

        if found:
            with open("plants.json", "w", encoding="utf-8") as file:
                json.dump(loaded_plants, file, indent=4)

            print("Medicinal use added and saved successfully.")
        else:
            print("Plant not found.")

    elif choice == "4":
        export_to_csv(loaded_plants)

    elif choice == "5":
        print("Over and Out !")
        break

    else:
        print("Invalid Choice")

