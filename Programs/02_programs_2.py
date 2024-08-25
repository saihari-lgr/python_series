from twisted.words.protocols.irc import split

from Utils.core import area_of_triangle, prime_check

# Area of triangle
# demo = 'Area of triangle'
# print(f'**** {demo} *****')
# s11 = float(input('Enter first number \t:'))
# s22 = float(input('Enter second number \t:'))
# s33 = float(input('Enter third number \t:'))
# # calculating semi parameter
# area = area_of_triangle(s11,s22,s33)
# print('Area of trinagle is %0.2f ' %area)

# input = int(input('Enter a number:\t '))
# if input >= 0:
#     res = 'Positive'
# else:
#     res = 'Negative'
#
# print(f'enter number: {input} is {res}')

# input = int(input('Prime Check: Enter a number:- '))
# prime_check(input)

print('Remove punctuations from word')
# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_string = "Hello World !! Welcome... to - new : programming"

no_punct = ""
for char in my_string:
    if char not in punctuations:
        no_punct = no_punct + char

print('Orginal string: \t', my_string)
print('Without punctutation: \t', no_punct)

print('Sort words in alphabetic order')
input1 = "Welcome you new Series"
new_input = [word.lower() for word in input1.split()]
new_input.sort()
print('Original String: \t',  input1)
print('Sorted String: \t',  new_input)

my_list = [1,2,3,4,5,6,7,8,9,10]
chunk_size = 2
for x in range(0,len(my_list),chunk_size):
    print(my_list[x:x+chunk_size])








