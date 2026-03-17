from datetime import datetime

now = datetime.now()

print("Hello, DMOS!")
print(f"Data curenta: {now.strftime('%Y-%m-%d %H:%M:%S')}")

name=input("Cum te cheama?")
print(f"Salut, {name}!")

if name.lower() == "daria":
    print("Boss detected.")
