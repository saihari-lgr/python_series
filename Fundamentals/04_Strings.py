#source https://docs.python.org/3/tutorial/introduction.html

#single quotes
greet = 'good morning'
print(greet)
#double quotes
print("have a nice day")

print('** Escape character')
print('don\'t go')
print("let's catch up")
print("\"You\" are wonderful")
print("1. Payment \n2. Accepted")


print('** Raw string')
print(r'c:\somepath\Adventure\Movies')  # adding r before  quote to make it as raw string

print('** multiple line span can achieve using tripe quotes')
print("""
    your milestone is 
    few steps away
    keep moving
""")

print('** String concatenation')
result = 'hello ' + 'world '
print(result)

reslt = 'Good ' 'Morning'
print(reslt)  # strings next to each other will automatically concatenated.This feature is useful when we want to break a long string

print('** String index')
# Note: start is always included and end is always excluded
result = 'ANIMAL'
print(result[0])
print(result[1])

print('** Negative index will start from right')
print(result[-1]) #----> L
print(result[-2]) # ----> A

print('** Slicing')
print(result[0:2]) # 0 included to 2 excluded  ----> AN
print(result[2:4]) # 2 included to 4 excluded  ----> IM
print(result[1:])  # from 1 position to end    ----> NIMAL
print(result[:2])  # from begining to position 2 ----> AN
print(result[-2:]) # character from second last to end ---->AL

print('** String are Immutable, Means Strings cannot be changed')
#result[0] = 'S'  #TypeError: 'str' object does not support item assignment

print('Built in string functions')
print('Lower case:\t ',result.lower())
print('Upper case:\t ',result.upper())
print('length :\t ', len(result))
print('Split :\t ',greet.split())  # by default split on space





