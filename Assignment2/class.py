def calculate_minimum_classes():
    students = int(input('Enter number of students: '))

    classes = (students // 30) +1

    students_in_each_class = students // classes

    remainder_students = students % classes

    class_allocation = {}

    for i in range(1, classes + 1):
        if i <= remainder_students:
            class_allocation[f"Class {i}"] = students_in_each_class + 1
        else:
            class_allocation[f"Class{i}"] = students_in_each_class

    print(f"Proposed Allocation: {classes} classes")
    print(class_allocation)

calculate_minimum_classes()