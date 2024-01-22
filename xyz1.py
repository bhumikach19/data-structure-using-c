my_file=open('test.txt') #reads all the lines of the file but one line at a time
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
my_file.close()