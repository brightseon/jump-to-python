import os

# print(os.path.join(os.getcwd()))
os.chdir(os.getcwd())

result = os.popen('ls')

print(result.read())
