def read_file():
    with open(r"C:\Users\Gokul\Documents\output.txt") as f:
        print(f.read())
        f.close()
read_file()