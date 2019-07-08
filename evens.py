def even_number_of_evens(num):
    if num == []:
        return False
    else:
        evens = 0

    for number in num:
        if number % 2 == 0:
            evens += 1

    if evens == 0:
        return False
    else:
        return evens % 2 == 0


assert even_number_of_evens([]) == False, 'No numbers'
assert even_number_of_evens([2]) == False, 'One even number'
assert even_number_of_evens([2, 4]) == True, 'Two even numbers'
assert even_number_of_evens([2, 3]) == False, 'Two numbers, only one even'
assert even_number_of_evens(
    [2, 3, 4, 5, 6]) == False, 'Uneven amount of even numbers'
assert even_number_of_evens(
    [2, 3, 4, 9, 10, 12]) == True, 'Even amount of even numbers'
assert even_number_of_evens([1, 3, 9]) == False, 'No even numbers'

print('All test passed')
