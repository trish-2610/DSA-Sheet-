s = "Hello world"
words = s.split()
rev_lst = [word[::-1] for word in words]
result = " ".join(rev_lst)
print(result)
