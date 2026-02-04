#총 10개 테스트
#배열 크기는 100x100 동일 / 동일 최대값은 그냥 하나의 값만

for i in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(1, 101)]

    #각 합들 담을 곳
    max_val = 0

    for y in range(100):
        sum_row = 0
        sum_columns = 0
        for x in range(100):
            sum_row += arr[y][x]
            sum_columns += arr[x][y]

        if sum_row > max_val : max_val = sum_row
        if sum_columns > max_val : max_val = sum_columns

    sum_cross_r = 0
    sum_cross_l = 0

    for y in range(100):
        sum_cross_r += arr[y][y]
        sum_cross_l += arr[y][99-y]

    result = max(max_val, sum_cross_r, sum_cross_l)

    print(f'#{t} {result}')