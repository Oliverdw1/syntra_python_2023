# Write a lambda function that returns the number of unique elements in an iterable.
# This could be the number of unique characters in a string, or the number of unique elements in a list, tuple, etc.
# If the iterable received by the lambda function is empty, then it should return 0.

x = lambda iterable: len(set(iterable))
l = [1,2,3,2,4,2,5,1]
print(x(l))