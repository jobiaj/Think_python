def find(word, letter,i):
    index = i
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    print "The letter not in the searched content"
print find("abcde","a" , 2 )
