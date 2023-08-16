base_url = "https://codefirstgirls.com/"
current_url = base_url
history = []

while True:
    print("You are currently on the URL", current_url)

    if current_url == base_url:
        print("Where are you clicking?")
        print("Options: Courses, Opportunities")
    elif current_url == base_url + "courses":
        print("Where are you clicking?")
        print("Options: CFGDegree, Back")
    elif current_url == base_url + "opportunities":
        print("Where are you clicking?")
        print("Options: Ambassadors, Back")
    elif current_url == base_url + "courses/cfgdegree":
        print("Where are you clicking?")
        print("Options: Back")
    elif current_url == base_url + "opportunities/ambassadors":
        print("Where are you clicking?")
        print("Options: Back")

    choice = input()

    if choice == "Courses" and current_url == base_url:
        current_url = base_url + "courses"
    elif choice == "Opportunities" and current_url == base_url:
        current_url = base_url + "opportunities"
    elif choice == "CFGDegree" and current_url == base_url + "courses":
        current_url = base_url + "courses/cfgdegree"
    elif choice == "Ambassadors" and current_url == base_url + "opportunities":
        current_url = base_url + "opportunities/ambassadors"
    elif choice == "Back":
        if history:
            current_url = history.pop()
        else:
            current_url = base_url

    history.append(current_url)


# Time complexity is: O(1) and the space complexity is O(n)