# Write code for algorithm 5 below
def palindrome(str):
    str = str.join(char.lower() for char in str if char.isalnum())
    return str == str[::-1]


word1 = "racecar"
word2 = "Python"
print(palindrome(word1))
print(palindrome(word2)) 