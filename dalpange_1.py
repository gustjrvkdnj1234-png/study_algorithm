t = int(input())

#우하좌상
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for tc in range(1, t+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]

    y, x = 0, 0
    current = 1
    idx = 0

    while current <= n*n:
        arr[y][x] = current

        ny = y + dy[idx]
        nx = x + dx[idx]

        if ny < 0 or ny >= n or nx < 0 or nx >= n or arr[ny][nx]:
            idx = (idx + 1) % 4
        
        current += 1
        y = y + dy[idx]
        x = x + dx[idx]

    print(f'#{tc}')
    for i in range(n):
        print(*arr[i])