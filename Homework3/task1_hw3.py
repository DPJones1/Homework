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

# The time complexity of the solution is an efficient one, with the size of the names.txt file being
# able to grow larger, but the code which runs through the name will not need to be adapted or made larger.
# Using deque means that it will save time in that it alters the text file into a queue ready to be ordered.
# The space complexity of the code will correlate to the amount of names that will be within deque therefore the
# performance will be adapted to the size of the file it is drawing from.