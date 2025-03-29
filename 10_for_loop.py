#1.for loop program
prices=[23, 56, 90, 100, 140]
print('Total sum: ', sum(prices))
sum_ = 0
for i in prices:
    sum_ += i
print(sum_)

#2. Nested loop program
print("Matrix is:")
for x in range(3):
    for y in range(3):
        print(f'({x},{y})', end="")
    print("\n", end="")

#3. printing F letter program
print("\n")
print("Printing F letter:")
num = [5,2,5,2,2]
for i in num:
    for j in range(i):
        print('x', end="")
    print("")