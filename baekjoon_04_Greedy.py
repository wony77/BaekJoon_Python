def solution(Gram1):
    bong = 0
    while Gram1 >= 0:
        if Gram1 % 5 == 0:
            bong = bong + (Gram1//5)
            break
        Gram1 -= 3
        bong += 1

        if Gram1 < 0:
            bong = -1
            break

    return bong

Gram = int(input('상근이가 배달해야할 그램 수: '))
print(solution(Gram))