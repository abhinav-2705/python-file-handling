with open("data.txt", "w") as f:
    f.write("Hello File")

with open("data.txt", "r") as f:
    print(f.read())
