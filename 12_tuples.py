print(''' Pointers:-
1. Tuple is immutable just like string.
2. It is similar to list but cannot be modified after creation.
3. t1=(1,2,3,4) created using parentheses unlike list which is created using square bracket.
4. Supports multiple assignment at a time''')

coordinates=(1,2,7)
a,b,c=coordinates #unpacking feature in tuple/list
print(f'{a}, {b}, {c}')