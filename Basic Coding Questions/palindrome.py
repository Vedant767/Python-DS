def palindrome(val):
    if val == val[::-1]:
        return True
    return False

print(palindrome("700100"))