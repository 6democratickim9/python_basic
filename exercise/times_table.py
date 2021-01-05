def times_table(number):
    if 1<=number<=9:
        for a in range(1,10):
            print(number,"X",a,"=",number*a)
    else:
        print("구구단 게임을 종료합니다.")


print("구구단 몇 단을 계산할까요?(1~9) ")
number=int(input())
times_table(number)