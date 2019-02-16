import os
x = [[7, 8, 9],[4,5,6],[1,2,3]]
z = x
result = []
count = 0

def display_board(lst):
    print('        |     |')
    print('     ' + str(lst[0][0]) + '  |  ' + str(lst[0][1]) + '  |' + '  ' + str(lst[0][2]))
    print('        |     |')
    print('----------------------')
    print('        |     |')
    print('     ' + str(lst[1][0]) + '  |  ' + str(lst[1][1]) + '  |' + '  ' + str(lst[1][2]))
    print('        |     |')
    print('----------------------')
    print('        |     |')
    print('     ' + str(lst[2][0]) + '  |  ' + str(lst[2][1]) + '  |' + '  ' + str(lst[2][2]))
    print('        |     |')

def position_selected(position,current_list,star_or_hash):
    global z
    global result
    for i in current_list:
        y = [j if j != position else star_or_hash for j in i]
        result.append(y)
    z = result
    result = []

def verification(current_list):
    for i in range(0,len(current_list[0])):
        temp = ''
        for j in range(0, len(current_list)):
            temp = temp + str(current_list[j][i])
        if temp == '***':
            print('player 1 is the winner')
            display_board(current_list)
            quit()
        if temp == '###':
            print('player 2 is the winner')
            display_board(current_list)
            quit()

    for i in z:
        if ''.join(str(i)) == '***':
            print('player 1 is the winner')
            display_board(current_list)
            quit()
        if ''.join(str(i)) == '###':
            print('player 2 is the winner')
            display_board(current_list)
            quit()
    for i in current_list:
        left_right = ''
        right_left = ''
        for j in range(0,len(i)):
            left_right = left_right + str(i[j])
        for j in range(len(i) - 1, -1, -1):
            right_left = right_left + str(i[j])
        if left_right == '***':
            print('*************************')
            print('*player 1 is the winner**')
            print('*************************')
            display_board(current_list)
            quit()
        if right_left == '###':
            print('*************************')
            print('*player 2 is the winner**')
            print('*************************')
            display_board(current_list)
            quit()


print('This is the NUMPAD for Tic-tac-Toe Game!!!!')
display_board(x)

while True:
    selection = int(input('Player 1 Enter your Position '))
    count = count + 1
    position_selected(selection, z, '*')
    display_board(z)
    verification(z)
    if count == 9:
        print('It is a draw')
        break
    selection = int(input('Player 2 Enter your Position '))
    count = count + 1
    position_selected(selection, z, '#')
    display_board(z)
    verification(z)
