A = input("8진수 입력 : ")
Change = [4,2,1]

Change_eight = ''
B = list(A)

if A != '0':
    for num in B:
        C = int(num)
        for i in range(0,len(Change)):
            if (C - Change[i]) >= 0:
                Change_eight += '1'
                C -= Change[i]
            else:
                Change_eight += '0'
    K = 0
    while(True):
        if Change_eight[K:K+1] == '0':
            Change_eight = Change_eight[K+1:]
        else:
            break
else:
    Change_eight += '0'
    
print(Change_eight)