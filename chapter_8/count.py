def count(words,letter):
     count = 0
     for i in words:
           if i == letter:
               count = count + 1
     print count

count("banana","n")
