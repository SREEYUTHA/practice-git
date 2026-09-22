def palindrome(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    s = s.replace(" ", "").lower()
    return s == s[::-1]