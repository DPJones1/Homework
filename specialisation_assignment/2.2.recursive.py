#recursive 
def number_of_squares(n):
    if n == 1:
        return 1
    return n * n + number_of_squares(n - 1)

print(number_of_squares(2))