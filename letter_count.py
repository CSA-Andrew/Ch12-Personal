#Andrew Hilton Comp Prog 3/5/18 lettercount
def countAll(word):
    dictionary={}
    for letter in word:
        dictionary[letter] = 0
    for letter in word:
        dictionary[letter] += 1
    return dictionary
x=input("Enter word to count frequency")
print(countAll(x))
