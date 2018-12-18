def is_polindrome(s):
    if s[:: -1] == s:
        return True
    return False

S = input("Input your String: ")

if is_polindrome(S):
    print("Results: \n" + S + "is a Polidrome." )
else:
    print("Results: \n" + S + "is not a Polidrome." )