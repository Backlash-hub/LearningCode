data= 'From william.pevytoe@gmail.com Sat Jan 09:14:16 2008'
wasd = data.find('@')
print(wasd)

dsaw = data.find(' ',wasd)
print(dsaw)

host = data[wasd+1 : dsaw]
print(host)