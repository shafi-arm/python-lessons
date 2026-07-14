myList = []
print("Empty list : ", myList)

myList2 = [11,4,7,99,3,12]
print(myList2)

print(myList2[0])

print(myList2[-1])

print(myList2[1:3])

print('my list :', myList2)

myList2.append(33)
print(myList2)

myList2.remove(99)
print(myList2)

myList2.pop()
print(myList2)

myList2.pop(2)
print(myList2)

print("current list :", myList2)
myList2.sort()
print("After sorting :", myList2)

myList2.reverse()
print(myList2)

print(myList2[::-1])