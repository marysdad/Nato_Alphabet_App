import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    try:
        word = input("Enter a word").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("you cannot enter number; it has be letters, try again")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()

