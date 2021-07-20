# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
#동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 
# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

def coin(N,K):
    coin1 = []
    cnt = 0
    for i in range(N):
        coin1.append(int(input()))
    coin1.sort(reverse=True)
    
    for co in coin1:
        cnt += K//co
        K %= co
    return cnt

N, K = list(map(int,input().split()))
print(coin(N,K))