fname = ('E:/PY4E/mbox-short.txt')
#fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

lst = list()
for line in fh:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    lst.append(words[1])
    count = count + 1
    continue

print(*lst,sep='\n')
print("There were", count, "lines in the file with From as the first word")