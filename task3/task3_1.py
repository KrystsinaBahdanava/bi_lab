# 1 Use a list comprehension to construct the
# list ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']

list1 = ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']

print(list1)

# 2 Use a slice on the above list to construct the
# list ['ab', 'ad', 'bc'].

list2 = list1[::2]

print(list2)

# 3 Use a list comprehension to construct
# the list ['1a', '2a', '3a', '4a'].

list3 = ['1a', '2a', '3a', '4a']

print()

# Compare lists (i thought there was such task)

print("Are list1 and list3 the same: ")

print(set(list1) == set(list3) & set(list1) and
      set(list3) == set(list3) & set(list1))

# 4 Simultaneously remove the element '2a' from
# the above list and print it.

del list3[1]

print()

print("After deleting: ")

print(list3)

# 5 Copy the above list and add '2a' back
# into the list such that the original is still missing it.

list4 = list3[:]

list4.append("2a")

print()

print(list4)

print(list3)
