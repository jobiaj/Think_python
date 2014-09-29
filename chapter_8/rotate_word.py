def rotate_word(word,n):
     x =''
     for i in word:
        b = ord(i)
        c = b + n
        d = chr(c)
        x = x+d
     print x
rotate_word("abc",3)
