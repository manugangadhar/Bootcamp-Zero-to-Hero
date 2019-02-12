import time
x = 7
y = x ** 2

while 1:
    if len(str(y)) == 1:
        time.sleep(5)
        print(y)
        y = y ** 2
        print(y)
        continue
    else:
        time.sleep(5)
        print(y)
        digit_list = list(str(y))
        temp_list = []
        for i in digit_list:
            temp_list.append(int(i)**2)
        if sum(temp_list) == 1:
            print('It is a lucky number')
            break
        else:
            y = sum(temp_list)
            continue

