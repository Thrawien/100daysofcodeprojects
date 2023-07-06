with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# w for mode mean "writable" default is read only, a is for "append"
# if no file exists and you set mode to w, it will create a new file for you
# with open("my_file.txt", mode="a") as file:
    # file.write("Love you Alex!.")

# with open("new_file.txt", mode="w") as file:
    # file.write("New text.")