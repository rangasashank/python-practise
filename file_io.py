# File IO basics
"""
"r" - Open file for reading - default
"w" - open file for writing
"x" - creates file if not exists
"a" - Add more content to a file
"t" - text mode - default
"b" - binary mode
"+" - read and write

"""

f = open("sashi.txt", "rt")
print(f.readlines())
# content = f.read()
# print(f.readline())
# print(f.readline())
# print(f.readline())

# for line in f:
#     print(line, end = "")

#  print(content)
# content = f.read(3433)
# print("1", content)

f.close()