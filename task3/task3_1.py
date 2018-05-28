# 1 Use a list comprehension to construct the
# list ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']

list1 = [a + b for a in 'ab' for b in 'bcd']

print(list1)

# 2 Use a slice on the above list to construct the
# list ['ab', 'ad', 'bc'].

list2 = list1[::2]

print(list2)

# 3 Use a list comprehension to construct
# the list ['1a', '2a', '3a', '4a'].

list3 = [str(i) + "a" for i in range(4)]

print(list3)

# 4 Simultaneously remove the element '2a' from
# the above list and print it.

print(list3.pop(1))

print("After deleting: ")

print(list3)

# 5 Copy the above list and add '2a' back
# into the list such that the original is still missing it.

list4 = list3[:]

list4.append("2a")

print(list4)

print(list3)
