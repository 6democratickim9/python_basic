'''names = ["Jin", "Sungchul", "Ronaldo", "Hong", "Seo"]
positions = ["MF", "DF", "CF", "WF", "GK"]
numbers = [10, 15, 20, 3, 1]

players = [[name, position, number ]for name, position, number in zip(names, positions, numbers)]
print(players)
print(players[0])'''

class SoccerPlayer(object):

    def __init__(self, name, position, back_number=20):
        print('생성자 함수 호출됨')
        #속성들
        self.name = name
        self.position = position
        self.back_number = back_number
    #back_number 속성을 변경하는 메서드
    def change_back_number(self, new_number):
        print("선수의 등번호를 변경합니다 : From %d to %d" % (self.back_number, new_number))
        self.back_number = new_number
    #객체주소 대신에 원하는 다른 속성값을 반환해주는 메서드
    def __str__(self):
        print('객체의 속성 값을 반환해주는 메서드')
        return "Hello, My name is %s. I play in %s in center Back number %d" % (self.name, self.position, self.back_number)
'''
player_objects = [SoccerPlayer(name, position, number) for name, position, number in zip(names, positions, numbers)]
print(player_objects[0])
'''
jinhyun = SoccerPlayer("Jinhyun", "MF", 10)
print(jinhyun)
dain = SoccerPlayer("둘리" , "GK",5)
print(dain)

print("현재 선수의 등번호는 : ",jinhyun.back_number)
jinhyun.change_back_number(5)
print("현재 선수의 등번호는 : ", jinhyun.back_number)

# 실행이 됐을떄만 메인 메서드 호출하는 것
# import 한 경우에는 main() 함수가 호출되지는 않는다.
