is_hot=input("Is day hot? ")

if is_hot:
    print('''It's a hot day
Drink plenty of water
    ''')
elif not is_hot:
    print('''It's a cold day
Wear warm clothes''')
else:
    print("It's a lovely day")

#Next program
credit=input("Enter your credit points: ")
if (int(credit)>200 and int(credit)<1000):
    is_credit_good=True
else:
    is_credit_good=False

price=500000
if is_credit_good:
    price -= (price*10)/100
else:
    price -= (price*20)/100
print('Down payment: ', price)


#3. Program
name=input('Enter your name: ')
if len(name) < 3:
    print('Name must be least 3 character long')
elif len(name)>50:
    print('Name can be maximum of 50 characters')
else:
    print('name looks good')