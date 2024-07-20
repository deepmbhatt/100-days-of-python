with open("day24mailmerge/names.txt") as names_file:
    names = names_file.readlines()
with open("day24mailmerge/letter/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        new_letter = letter_contents.replace("[Name]", name.strip())
        with open(f"day24mailmerge/letter/letter_for_{name.strip()}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
