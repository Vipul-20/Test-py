def reverser_char(char):
    alphabet='abcdefghijklmnopqrstuvwxyz'

    # return char if not valid alphabet

    if char not in alphabet and char not in alphabet.upper():
        return char

    if char in alphabet.upper():
        alphabet=alphabet.upper()
    # Find index of character
    index_of_char=alphabet.index(char)
    #Find opposite index 
    opposite_index = 26 - index_of_char
 
    opp_char=alphabet[opposite_index -1] 
    return opp_char

x = reverser_char('b')
# print(x)
# print( reverser('a')=='z')
# print( reverser('b')=='y')
# print( reverser('c')=='x')
"""
Reverse a character either lower or capital
"""
def atbash(txt):
    reverseTxt=""
    for char in txt:
        reverseTxt += reverser_char(char)
    return reverseTxt    

print(atbash("Hello world!") == "Svool dliow!")
