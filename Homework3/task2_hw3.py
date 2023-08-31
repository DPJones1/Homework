#8,15,22,29,36,... For example:
# num_in_seq(1) = 8
# num_in_seq(5) = 36
# num_in_seq(10) = 71

def num_in_seq(num):
    if num == 1:
        return 8
    else:
        return num_in_seq(num -1) + 7

print(num_in_seq(1))
print(num_in_seq(5))
print(num_in_seq(10))
