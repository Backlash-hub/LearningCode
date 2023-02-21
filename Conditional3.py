rawstr = input('Enter a number:')
try:
    inval = int(rawstr)
except:
    ival = -1
    
if inval > 0 :
    print('Nice Work')
else:
    print('Not a number')