
#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number 
# of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the
# person who sent the mail. The program creates a Python dictionary that maps the sender's mail address
# to a results of the number of times they appear in the file. After the dictionary is produced, the program 
# reads through the dictionary using a maximum loop to find the most prolific committer

name = ('E:/PY4E/mbox-short.txt')
#name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

results = dict()


for line in handle:
    if not line.startswith('From'): continue
    line = line.rstrip()
    words = line.split()
    for email in words:
        email = words[1]
        results[email] = results.get(email,0) + 1
                        
bigcount = None
bigemail = None
for email,count in results.items():
  if bigcount is None or count > bigcount:
     bigemail = email
     bigcount = count

print(bigemail, bigcount)