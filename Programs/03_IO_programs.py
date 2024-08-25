
print('Reading content of a file')
# read_data = []
with open("../lib/greet.txt") as fl:
    read_data = fl.readlines()

print('Raw File Content: \n',read_data)
#removing new line characters
read_data_content = [x.strip() for x in read_data]
print('Formatted File Content: \n',read_data_content)

