def capitalize_all(i):
    res = []
    for s in i:
        res.append(s.capitalize())
    return res
def capitalize_nested(d):
      b = []
      for i in d:
		c = capitalize_all(i)
                b.append(c)
      return b
           
print capitalize_nested([["jobi","najeeb"],["athul","fasal"]])
