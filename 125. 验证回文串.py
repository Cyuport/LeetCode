def isPalindrome(s: str) -> bool:
    s = ''.join(x for x in s if x.isalnum()).lower()
    return s == s[::-1]

if __name__ == '__main__':
    print(isPalindrome("A man, b plan, a canal: Panama"))