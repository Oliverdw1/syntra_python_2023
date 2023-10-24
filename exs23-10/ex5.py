def palindrome(string):
    return string == string[::-1]

print(palindrome("oliver"))
print(palindrome("racecar"))