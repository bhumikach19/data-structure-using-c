my_file=open('test.txt') #reads the file
print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.close()