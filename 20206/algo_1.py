t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    sample = list(map(int, input().split()))
    p_code = list(map(int, input().split()))

    result = 0
    idx = 0

    for i in range(n):
        if sample[i] == p_code[idx]:
            idx += 1

        if idx == k:
            result = 1
            break

    print(f'#{tc} {result}')