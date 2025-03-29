lst=[1,2,3,49,5,6,7,12]
print(max(lst))

#2D list
mat=[[1,2,3],[4,5,6],[7,8,9]]
for i in mat:
    i[0] += 1
    print(i)

#METHODS in list
num = [3,2,1,3,3,6,7,8,9,0,0]
num.remove(3)
num.pop(0)
num2=num.copy()
num.sort()
print(num, "mem_loc: ", id(num))
print(num2, "mem_loc: ", id(num2))

#remove duplicates from list
for i in num:
    if num.count(i) == 2:
        for j in num:
            if i == j:
                num.remove(j)
print(num)
