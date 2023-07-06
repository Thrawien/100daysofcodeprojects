PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt", "r") as names_file:
    # returns a list containing each line in the file as a list item
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    letter = letter_file.read()
    for name in names:
        # The strip() method removes any leading, and trailing whitespaces
        stripped_name = name.strip()
        # The replace() method replaces a specified phrase with another specified phrase
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)