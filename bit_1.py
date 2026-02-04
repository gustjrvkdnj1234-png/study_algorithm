print(1)
print(1 << 1) # 0010 = 2
print(1 << 3) # 1000 = 4

attack = 0
jump = 0
move = 0

def attack():
    global attack
    attack = 1

if attack:
    print('공격 중입니다.')

#상태값이 늘어난다면, 