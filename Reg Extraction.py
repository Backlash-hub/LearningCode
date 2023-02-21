#import re


# ##################################

# #hand = open('E:/PY4E/mbox-short.txt')
# #for line in hand:
# #    line = line.rstrip()
# #    if re.search('^From:', line) :
# #        print(line)

# ####################################

# x = 'My 2 favorite numbers are 8 and 32'
# y = re.findall('[0-9]+',x)
# print(y)

# x = 'My 2 favorite numbers are 8 and 32'
# y = re.findall('[aeiou]+',x)
# print(y)

# x = 'My 2 favorite numbers are 8 and 32'
# y = re.findall('[AEIUO]+',x)
# print(y)

# ########################################

# #Greedy
# x = 'From: Using the : character'
# y = re.findall('^F.+:', x)
# print(y)

# #Non Greedy
# x = 'From: Using the : character'
# y = re.findall('^F.+?:', x)
# print(y)


# #####################################

# x = "From williampevytoe@gmail.com Sat Jan 4 09:14:16 2008"
# y = re.findall('\S+@\S+', x)
# print(y)

# x = "From williampevytoe@gmail.com Sat Jan 4 09:14:16 2008"
# y = re.findall('From (\S+@\S+)', x)
# print(y)

# ######################################


# x = "From williampevytoe@gmail.com Sat Jan 4 09:14:16 2008"
# y = x.find('@')
# print(y)

# a = x.find(' ',y)
# print(a)

# host = x[y+1 : a]
# print(host)

# # x = "From williampevytoe@gmail.com Sat Jan 4 09:14:16 2008"
# words = x.split()
# email = words[1]
# pieces = email.split('@')
# print(pieces[1])

# #reg expression way from ^
# x = "From williampevytoe@gmail.com Sat Jan 4 09:14:16 2008"
# y = re.findall('@([^ ]*)', x)
# # print(y)

####################################

# import re
# hand =open('E:/PY4E/mbox-short.txt')
# numlist = list()
# for line in hand:
#     line = line.rstrip()
#     stuff = re.findall('X-DSPAM-Confidence: ([0-9.]+)', line)
#     if len(stuff) !=1 : continue
#     num = float(stuff[0])
#     numlist.append(num)
# print('Maximum:', max(numlist))

###################################

# import re
# x = 'We just received $10.00 for cookies'
# y = re.findall('\$[0-9.]+', x)
# print(y)

