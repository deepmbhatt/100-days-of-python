import pandas
nato_data_frame = pandas.read_csv("day26NATOalphabetproject/nato_phonetic_alphabet.csv")

#Loop through rows of a data frame
#for (index, row) in nato_data_frame.iterrows():
    #print(row.letter)
    #print(row.code)

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter a word: ").upper()
is_on = True
while is_on:
    try:
        name_list = [nato_dict[letter] for letter in name]
        is_on = False
    except KeyError:
        print("Sorry only letters in the alphabet please.")
        name = input("Enter a word: ").upper()

print(name_list)

