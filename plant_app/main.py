from plants.operations import add_use,create_dict,export_to_csv,view_plants
from storage.json_storage import load_plants,save_plants
import json


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

        save_plants(loaded_plants)
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
            save_plants(loaded_plants)

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