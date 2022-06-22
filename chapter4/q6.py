input1 = input('입력해주세요: ')

f1 = open('test.txt', 'a')
f1.write(f'{input1}\n')
f1.close()

f2 = open('test.txt', 'r')
print(f2.readlines())
