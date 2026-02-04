import sys
sys.stdin = open('input.txt', 'r')

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    delta = [0] * (n + 1) #마지막 인덱스 버림
    p = int(input())
    for _ in range(p):
        start, end, cost = map(int, input().split())
        delta[start] += cost
        delta[end + 1] -= cost

    current_delta = 0 #현재 시점 변화량
    for i in range(n):
        current_delta += delta[i]
        arr[i] += current_delta

    print(f'#{tc}', *arr)
    #print(f'#{tc} {" ".join(map(str, arr))}')
    