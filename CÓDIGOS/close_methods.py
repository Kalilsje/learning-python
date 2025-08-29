f = open("emails.txt", "r")
try:
    print(f.read(10))
except Exception as e:
    print(e)
finally:
    print("Arquivo sendo fechado...")
    f.close()

with open("emails.txt", "r") as f:
    print(f.read(10))