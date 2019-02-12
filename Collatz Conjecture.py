x = int(input('Enter an positive number'))
steps = 0
while 1:
    if x % 2 == 0:
        x = x / 2
        steps = steps + 1
        if x == 1:
            print('reached 1 with number of steps = {}'.format(steps))
            break
        continue
    else:
        x = (x * 3) + 1
        steps = steps + 1
        if x == 1:
            print('reached 1 with number of steps = {}'.format(steps))
            break
        continue