current_year = 2021
birth_year = 2006

current_month = 8
birth_month = 7

a = (current_year - birth_year) == 16 # True
b = current_month == birth_month    # False
if a and b:   # True and False
    print("Happy sweet 16th month")


f = file_exists(".....")
if not f:
    print("File does not exist")

a = 10
b = 20

if b != 0:
    print(a / b)


nums = []
if not nums.empty():
    print (nums)


a      b       a and b
False  False   False
False  True    False
True   False   False
True   True    True

a      b       a or b  not (a or b)
False  False   False   True
False  True    True    False
True   False   True    False
True   True    True    False

a      not a
False  True
True   False

a      b      c       (a and b) or c
False  False  False   False
False  False  True    True
False  True   False   False
False  True   True    True
True   False  False   False
True   False  True    True
True   True   False   True
True   True   True    True



0, 1 ,,,, inf
False, True
(not((a or b) and c)) and (d or f)
(( a + b) * (c - d)) / e

  1
  010
+ 010
  100
