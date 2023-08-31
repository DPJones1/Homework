def unique_consanants(s):
    consanants = "bcdfghjklmnpqrstvwxyz"

    s = s.lower()

    unique_consanants = set()

    for character in s:
        if character in consanants and s.count(character) == 1:
            unique_consanants.add(character)

    return len(unique_consanants)

user_input = input("please input a word: ")
print(f"The amount of unique consonants in your word are: {unique_consanants(user_input)}")

#The time complexity of this would be: O(n2)
#The space complecity of this would be: O(n)