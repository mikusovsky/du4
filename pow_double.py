def pow(i):
    return i*i

file = open('test.in', 'r')

for line in file:
    print(pow(int(line)))