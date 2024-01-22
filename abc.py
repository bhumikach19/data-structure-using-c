import re   #string matching
search='search within this'
print(re.search('this',search))
if(re.search('this',search)):
    print(True)


a=re.search('this',search)
print(a.start())
print(a.end())
print(a.group())