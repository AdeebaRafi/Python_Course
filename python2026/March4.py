def is_palindrome(a):
    left = 0
    right = len(a) - 1
    while left < right:
        if a[left] != a[right]:
            return False
        left+=1
        right-=1
    return True
text = "male"
text1 = "MadaM"
print(is_palindrome(text))
print(is_palindrome(text1))
