def palindrome(word):
    n = 0
    while n < len(word):
        if word[n] != word[-n-1]:
            return False
        else:
            n += 1
    return True
