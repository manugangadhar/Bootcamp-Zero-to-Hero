x = 3
binary = []
binary_sum = []
if x == 0:
    print(0)
    quit()
else:
    i = 0
    while True:
        if 2 ** i < x:
            binary.append(0)
            i = i + 1
        elif 2 ** i == x:
            binary.append(1)
            binary.reverse()
            print(binary)
            quit()
        else:
            i = i - 1
            binary[i] = 1
            break
    binary_sum.append(2**i)
    i = i - 1
    while True:
        if sum(binary_sum) + 2 ** i == x:
            binary[i] = 1
            binary.reverse()
            print(binary)
            quit()
        elif sum(binary_sum) + 2 ** i < x:
            binary_sum.append(2**i)
            binary[i] = 1
            i = i - 1
        else:
            binary[i] = 0
            i = i - 1




