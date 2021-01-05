import random

guess_number=random.randint(1,100)
count=0
print("숫자를 맞춰주세요: ")
input_num=input()

while input_num!=guess_number:
    if int(input_num)>guess_number:
        print("숫자가 너무 큽니다")
        count+=1
        input_num = input()
    elif int(input_num)<guess_number:
        print("숫자가 너무 작습니다")
        count+=1
        input_num = input()
    else:
        print("정답입니다.",count,"회 카운트 되었습니다.")
        break

