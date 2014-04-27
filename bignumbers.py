## Big Numbers
print 'Big numbers'
while True:
    x = int(raw_input('Give me a number: '))
    y = int(raw_input('And another one: '))
    if x + y <= 99:
        print 'Small number'
        break
    elif x + y >= 101:
        print 'Big numbers'
        break
    else:
        print 'Neither big nor small'
        break
