fname = ('E:/PY4E/romeo.txt')
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for wrds in words:
        if wrds not in lst:
            lst.append(wrds)
lst=list(lst)
lst.sort()   
print(lst)