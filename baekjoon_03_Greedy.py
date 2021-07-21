# 그리디 알고리즘 ATM 
def ATM(people):
    delay = list(map(int,input().split()))
    delay.sort()
    time = 0
    for i in range(0, people):
        for j in range(0,i+1):
            time += delay[j]
    return time

people = int(input('기다리는 사람의 인원수: '))
print(ATM(people))
