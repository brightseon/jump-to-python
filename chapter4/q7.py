from resource import struct_rusage


test = open('test.txt', 'r')
str = test.read()
str = str.replace('java', 'python')

test2 = open('test.txt', 'w')
test2.write(str)
test2.close()
