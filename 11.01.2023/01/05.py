# a
# ['1a', '2a', '3a', '4a']

list1 = [str(i)+'a' for i in range(1, 5)]

print(list1)

list2 = ['a'+i for i in ['b', 'c', 'd']]
print(list2)
list3 = [j+i for j in ['a', 'b'] for i in ['b', 'c', 'd']]
print(list3)

list4 = [i*10 for i in range(1, 11)]
print(list4)
