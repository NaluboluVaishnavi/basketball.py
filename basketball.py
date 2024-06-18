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
