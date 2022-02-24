num = int(input())
for x in range(1, num + 1):
    t = ''
    for y in range(x):
        t = t + '*'
        j = '*' * y
        i = ' ' * (num - x)
    print(i + j + t)
