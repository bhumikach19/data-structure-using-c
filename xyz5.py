with open('test.txt',mode='a') as my_file:  #append a file ie adds extra bit at the last
    text=my_file.write(':D')
    print(text)