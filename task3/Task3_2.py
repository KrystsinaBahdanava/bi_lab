# Create the list ['a', 'b', 'c'], then create a tuple from that list.

list1 = ['a', 'b', 'c']

tup1 = tuple((list1[:]))

print(tup1)

# 2 Create the tuple ('a', 'b', 'c'), then create a list from that tuple.
# (Hint: the material needed to do this has been covered, but it's
# not entirely obvious)

tup2 = ('a', 'b', 'c')

list2 = list(tup2[:])

print(list2)

# 3 Make the following instantiations simultaneously:
# a = 'a', b=2, c='gamma'. (That is, in one line of code).

a, b, c = 'a', 2, 'gamma'

print(a)

print(b)

print(c)

# 4 Create a tuple containing just a single element which in turn
# contains the three elements 'a', 'b', and 'c'. Verify that the
# length is actually 1 by using the len() function.

tup3 = tuple([('a', 'b', 'c')])

print(tup3)

print(len(tup3))
