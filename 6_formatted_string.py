from datetime import date

name=input("enter you name: ")
msg=f'Hello {name}!!, Today is {date.today()}'
print(msg)

print(name.upper())
print(name)

#is string immutable? - YES
msg1='string is immutable'
print(msg1)
msg2 = msg1.replace('is', 'is always')
print('original string: ', msg1, ' memory_location: ', id(msg1))
print('replaced string is: ', msg2, ' memory_location: ', id(msg2))

#Hence, string is immutable. after applying replace() a new string is getting formed
