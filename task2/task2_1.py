my_str = input("write string: ")

my_str = my_str.casefold()

rev_str = my_str[::-1]

if list(my_str) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")
