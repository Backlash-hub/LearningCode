# Dictionary - A bag of values, each with its own lable
    #list - a linear collection of values

#bag = dict()
#bag['money'] = 12
#bag['candy'] = 3
#bag['tissue'] = 75

#print(bag)

#bag['candy'] = bag['candy'] + 2

#print(bag)

#########################

#counts = dict()
#names = ['Will', 'Mason', 'Kaitlyn', 'Franky', 'Will']
#for name in names :
#    if name not in counts :
#        counts[name] =1
#    else:
#        counts[name] = counts[name] + 1
#print(counts)

############################

#counts = dict()
#names = ['Will', 'Mason', 'Kaitlyn', 'Franky', 'Will']
#for name in names :
#    counts[name] = counts.get(name, 0) + 1
#print(counts)

############################

#counts = dict()
#line = input('Enter a line of text:')
#words = line.split()

#print('Words:', words)
#print('Counting...')

#for word in words:
#    counts[word] = counts.get(word,0) +1
#print('Counts', counts)

##############################

jjj = {'Will' : 1 , 'Mason' : 34 , 'Kaitlyn' : 65}
print(jjj)
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())