
def even(num):
    return num % 2 == 0


def count_even_numbers(num):
    count = 0
    for n in range(1, num + 1):
        if even(n):
            count = count + 1
    return count


print(count_even_numbers(10003))
