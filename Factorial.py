x = int(input("Enter an Integer"))
result = 1
if x != 0:
    for i in range(1,x):
        result = result * (x-i)
    result = result * x
else:
    result = 1
print(result)
