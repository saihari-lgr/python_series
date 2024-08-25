## source: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Data structure
letters = ['A','B','C','D','E','F','F','G','H']
print('Initial List', letters)

# 1. append(x) -- Adds element at the end of the list
letters.append('I')
print('After Append: ',letters)

# 2. extend() -  extend list by appending all the items from the iterable
letters.extend('J')
print('After  extend: \t',letters)

# 3. insert(i,x) - insert an item at given position
letters.insert(2,'C')
print('After  insert: \t',letters)

#4.  remove(x) - Removes the first item from list whose value is equal to x
letters.remove('C')
print('After remove: \t',letters)

#5.  pop[i] remove the item at the given position in the list and return it. if no index found pop() removes and return last index item
letters.pop(2)
print('After pop: \t',letters)

#6. index(x,[start],[end])  -- return zero based index in the list
print('After index: \t',letters.index('D'))

#7. count(x) : returns number of times x appears in the list
print('Count: \t',letters.count('F'))

#8. sort(*,key=None,reverse=False)
letters.sort()
print('After default sort: \t',letters)
letters.sort(reverse=True)
print('Reverse sort: \t',letters)

#9. copy() - Returns a shallow copy of the list
new_letters = letters.copy()
print('New List: \t',new_letters)


#10.  del() remove the elements from the provided index
# by index
del letters[0]
print('Del: ',letters)
# by slicing
del letters[0:3]
print('Del: ',letters)

print('** List Comprehensions')
# Example#1
# general way of looping
squares = []
for x in range(10):
    squares.append(x**2)
print('General way \t',squares)

# list comprehension
new_squares = []
new_squares = [(x**2) for x in range(10)]
print('comprehension way \t',new_squares)

my_set = []
for x in [1,2,3]:
    for y in [2,3,4]:
        if (x!=y):
            my_set.append((x,y))
print('General way \t',my_set)

new_my_set = []
new_my_set = [(x,y) for  x in [1,2,3] for y in [2,3,4] if x!=y]
print('Comprehension way \t',my_set)

print('** Quick Demos on Comprehensions')
t1 = [-4,-2,0,2,4]

new_t1 = [x for x in t1]
print('new t1 \t', new_t1)

new_t2 = [x for x in t1 if x > 0]
print('new t2 \t', new_t2)

abs_t1 = [abs(x) for x in t1]
print('abs_t1 \t', abs_t1)

tuple_t1 = [(x,x**2) for x in t1 if x > 0]
print('tuple_t1 \t', tuple_t1)

fruits = ['apple', 'mango',  'banana']
new_fruits = [ x.upper() for x in fruits]
print('fruits: \t', new_fruits)



