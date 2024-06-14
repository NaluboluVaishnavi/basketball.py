''''def max_possible_score(N, A):
    scores = [(i + 1) * A[i] for i in range(N)]
    max_current = scores[0]  
    max_global = scores[0]

    for i in range(1, N):
        max_current = max(scores[i], max_current + scores[i])
        if max_current > max_global:
            max_global = max_current
    return max_global
N = 5  
A = [1, -2, 3, 10, -4] 
print(max_possible_score(N, A))'''
inp1 = int(input())
inp2 = int(input())
arr = list(map(int,input().split()))
mx = -1
for i in range(0,len(arr)-inp2+1):
    temp = arr[j+inp2]
    k,s = 1,0
    for j in temp:
        s+=(j*k)
        k+=1
        if s>mx:
            mx=s
            print(mx)                                    