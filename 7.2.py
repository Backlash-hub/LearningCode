# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
data = 0.0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    space = line.find(':')
    data = data +float(line[space+1:])
    count = count + 1

print("Average spam confidence:", data/count)   


#   E:/PY4E/mbox-short.txt