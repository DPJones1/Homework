#non-recursive function
def number_of_squares(n):
    total = 0 
    for i in range (1, n + 1):
        total += i * i
    return total

print(number_of_squares(3))

