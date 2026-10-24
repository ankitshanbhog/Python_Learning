import random

number = [1,2,3,4,12,13,44,55]

print(random.choice(number))

import datetime

current = datetime.datetime.now()

cur_day = datetime.date.today()

print(cur_day.month)

from pathlib import Path

file_path = Path("plants.json")

if file_path.exists():
    print("S")

else:
    print("F")

