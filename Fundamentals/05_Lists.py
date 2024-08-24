# Lists
    ## Comma separated values (items)
    ## Represents using square brackets

even_numbers = [2,4,6,8,10]
odd_numbers = [1,3,5,7,9]
print(even_numbers)

# indexing and sliced
print(even_numbers[2])
print(even_numbers[0:4])

# concatenation
new_list = even_numbers + odd_numbers
print(new_list)

#  list are mutable, means value can be change
even_numbers[2] = 66
print(even_numbers)

# Variable assignment is a reference type, means it will not copy the entire data to new variable, rather it will point the reference to existing variable
new_even_numbers = even_numbers
print(new_even_numbers)
new_even_numbers[1] = 22
print('** printing both even and new even numbers')
print(even_numbers)
print(new_even_numbers)  # Note: values at position [1] is changed for both variables

#slicing operation will retuns the new list
slice_first_two_even = even_numbers[0:2]
print(slice_first_two_even)


# creating nested list
nest = [even_numbers,odd_numbers]
print('nested list', nest)

# common methods
print('** common methods')
#len
print('Length', len(slice_first_two_even))
# append() adds the new item at the end of list
even_numbers.append(12)
print('Append item', even_numbers)

#pop: removing element from the list, by default it will take -1, i,e last index
print('pop', even_numbers.pop())
print('After pop',even_numbers)

print('pop by position', even_numbers.pop(2))
print('After pop by position',even_numbers)

#sorting
even_numbers.sort()
print('Sort items: ', even_numbers)
even_numbers.reverse()
print('Reverse items: ', even_numbers)


#  remove elements from list
slice_first_two_even = []  # assigning empty list
print(slice_first_two_even)







