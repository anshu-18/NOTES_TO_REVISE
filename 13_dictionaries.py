#store the value in key-value pair
#It is unordered, mutable data structure

customer = {
    "name" : "smith",
    "age" : 40,
    "is_present" : True
}
print(customer["age"])


#2.next program
num=input("Enter your phone no: ")
number={
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five"
}
res = ""
for i in num:
    res += number.get(i, "!") + " "
print(res)