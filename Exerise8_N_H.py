user = input('username : ')
password = input('password : ')
if user == 'abc' and password == '123' :
    print('Welcome !')
    print('1.apple 10-')
    print('2.watermelon 20-')
    print('3.banana 30-')
    goods = int(input('>> '))
    volume = int(input('volume : '))
    if goods == 1 :
        print(10*volume, '-')
    elif goods == 2 :
        print(20*volume, '-')
    elif goods == 3 :
        print(30*volume, '-')
print('Thank You !')