n, x = map(int, input().split())
arr = list(map(int, input().split()))

window = sum(arr[:x])
max_window = window
max_day = 1

for i in range(n - x):
    window = window - arr[i] + arr[i+x]

    if window > max_window:
        max_window = window
        max_day = 1

    elif window == max_window:
        max_day += 1


if max_window == 0:
    print('SAD')
else:
    print(max_window)
    print(max_day)