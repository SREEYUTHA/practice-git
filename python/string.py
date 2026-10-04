def reverse_string(s):

    string1 = s.split()

    reverse_string = [word[::-1] for word in string1]
    return ' '.join(reverse_string)