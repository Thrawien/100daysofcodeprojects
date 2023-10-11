import pandas

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():

    word = input("Enter a word: ").upper()
    try:
        # Use list comprehension to extract the value from the dict and output that to a new list
        phonetic_list = [NATO_dict[letter] for letter in word]

    except KeyError:
        print("Sorry only letters in the alphabet please")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()