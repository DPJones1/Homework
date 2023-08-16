
def num_in_seq(num):
    first_value = 8
    value_difference = 7
    nth_value = first_value + (num - 1) * value_difference
    return nth_value

print(num_in_seq(1))
print(num_in_seq(5))
print(num_in_seq(10))

