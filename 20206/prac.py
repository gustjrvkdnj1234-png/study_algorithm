# 1. 랜덤으로 주어지는 샘플
t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())

# 2. k개의 길이의 패스코드
    sample = list(map(int, input().split()))
    p_code = list(map(int, input().split()))
#나오기만 하면 됌. 하나의 조건만. 앞에 인덱스가 나오면, 인덱스 올려.
    cnt = 0
    ans = 0
    for i in range(k):  #   앞에 부터 하나씩 나옴. 같은 수여도 얜 뭐 상관없지
        for j in range(n):
            while i < k:
                if sample[i] == p_code[j]:
                    cnt += 1
                    #처음 값은 거 구하고, 카운트 올려 카운트 값이 k개랑 같으면 1 되게 출력
                    #어쨌건, 같은 수만 연달아 찾으면 됌.
                    #k번째 까지

    if cnt == k:
        ans = 1


#3. 샘플에서 패스코드를 순차적으로 만들 수 있나? / 판단해라. 결과는 1 또는 0


    print(f'#{tc} {ans}')