import re   #password validation with condition 8 chars long with special char and should end with num
pattern1=re.compile(r"[a-zA-Z0-9%$#@]{8,}[0-9]$")
password='hik2ohaskdij#9'
check=pattern1.fullmatch(password)
print(check)