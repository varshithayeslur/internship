word = input("enter the word")
if word.endswith("y"):
    word = word [:len(word)-1] + "ies"
print(word)