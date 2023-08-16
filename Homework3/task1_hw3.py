from collections import deque

def arrange_queue(commands):
    queue = deque()

    for command in commands:
        action, name = command.split()

        if action == "JUMP":
            queue.appendleft(name)
        elif action == "JOIN":
            queue.append(name)

    return list(queue)

def main():
    input_filename = "names.txt"

    with open(input_filename, "r") as file:
        commands = [line.strip() for line in file]

    final_order = arrange_queue(commands)

    print("The updated final queue order:")
    for person in final_order:
        print(person)


if __name__ == "__main__":
    main()

# The time and space complexity: O(n)