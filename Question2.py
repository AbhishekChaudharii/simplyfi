test_cases = int(input(""))
# Number of test_cases we want

for i in range(test_cases):
    count = 0
    N,K = map(int,input().split())
    # N ==> number of players between Gi-Hun and Ali
    # K ==> height of both of them respectively.
    H = list(map(int,input().split()))
    # space-separated list of integers,denoting the heights of the players between Gi-Hun and Ali.
    for j in range(N):
        if H[j]>K:
            count+=1
    print(count)        


