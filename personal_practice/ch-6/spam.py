p1 = 'Make a lot of money'
p2 = 'buy now'
p3 = 'subscribe this'
p4 = 'click this'

L = ['Make a lot of money','buy now','subscribe this','click this']

message = input('Please enter a message: ')

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print('The message is spam')
else:
    print('The message is not spam')
    
    
if((message in L) or (message in L) or (message in L) or (message in L)):
    print('The message is spam')
else:
    print('The message is not spam')
    
