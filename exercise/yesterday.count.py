'''
yesterday.txt 파일을 읽어서
YESTERDAY(다 upper로 바꿔서),Yesterday,yesterday가 몇 번 나오는지 찾아보기
yesterday_lyric.upper().count('YESTERDAY')
yesterday_lyric.count('Yesterday')
yesterday_lyric.count('yesterday')
'''
yesterday=open("C:\mypython\python_programming_stu\exercise\yesterday.txt",'r')
yesterday_lyric=yesterday.readlines()
print(yesterday_lyric)
'''
upper_yes = yesterday_lyric.upper().count('YESTERDAY')
big_yes = yesterday_lyric.count('Yesterday')
small_yes = yesterday_lyric.count('yesterday')

print("The word 'YESTERDAY' came out ",upper_yes,"times ")
print("The word 'Yestderday' came out ",big_yes,"times" )
print("The word 'yesterday' came out ",small_yes,"times")
'''