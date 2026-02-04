import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_val = 0
    max_y, max_x = 0, 0

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for y in range(n):
        for x in range(n):
            current_sum = arr[y][x]

            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                if 0 <= ny < n and 0 <= nx < n:
                    current_sum += arr[ny][nx]
            
            if current_sum > max_val:
                max_val = current_sum
                max_y, max_x = y, x


    print(f'#{tc} {max_val} {max_y} {max_x}')