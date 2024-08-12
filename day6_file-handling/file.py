filepath= 'file.txt'
file = open(filepath, 'r')
print(file.read().replace('', '&'))
file.close()

with open(filepath, 'r') as file:
    print(file.read())
