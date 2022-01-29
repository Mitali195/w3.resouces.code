#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

nums = input('Enter numbers separated by comma:')
list = nums.split(",")
tuple = tuple(list)
print("List:",list)
print("Tuple:",tuple)
