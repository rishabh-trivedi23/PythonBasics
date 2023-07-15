placeholder = "[name]"
with open("names.txt") as f1:
    names = f1.readlines()
with open("letter.txt", mode="r") as f2:
    letter = f2.read()
    for name in names:
        new_name = name.strip()
        new_letter = letter.replace(placeholder, new_name)
        with open ("../output/letter_"+new_name+".txt", mode ="w") as f3:
            f3.write(new_letter)