class SoccerPlayer(object):
    # 생성자 함수 - 객체 생성될 떄 호출
    def __init__(self, name, position, back_number=30):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self, new_number):
        print("선수의 등번호를 변경합니다 : From %d to %d" % (self.back_number, new_number))
        self.back_number = new_number

    def __str__(self):
        return "Hello, My name is %s. I play in %s in center Back Number %d" % (self.name, self.position,self.back_number)

def main():
    # 객체생성
    jinhyun = SoccerPlayer("Jinhyun","MF",10)
    print(jinhyun)

    dolly = SoccerPlayer("둘리", "GK")
    print(dolly)

    print("현재 선수의 등번호 :" ,jinhyun.back_number)
    jinhyun.change_back_number(5)
    print("현재 선수의 등번호: ", jinhyun.back_number)

# 실행했을 경우에만 main() 함수를 호출 python python_class.py(tab 누르기)
# import한 경우에는 main 함수 호출되지 않음
if __name__=="__main__":
    main()
