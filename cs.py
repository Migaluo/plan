import random


def fun():
    choose = input('your choose:(B/S)')
    flag = False
    point1 = random.randrange(1, 7)
    point2 = random.randrange(1, 7)
    point3 = random.randrange(1, 7)
    print('The point is: ')
    print(point1, point2, point3)
    if 11 <= (point1 + point2 + point3) <= 18:
        flag = not flag
    else:
        flag = flag

    if flag and choose == 'B':
        return 'you win'
    if not flag and choose == 'S':
        return 'you win'
    return 'you lose'


count = 0
while count < 3:
    count += 1
    print(fun())