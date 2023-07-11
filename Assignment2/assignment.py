def is_isogram(input_str):
    input_str = input_str.lower()

    letters_counted = set()

    for letter in input_str:
        if letter in letters_counted:
            return False
        else:
            letters_counted.add(letter)
            return True

word = input("Please enter a word: ")
if is_isogram(word):
    print(f"{word} is an isogram")
else:
    print(f"{word} is not an isogram")





