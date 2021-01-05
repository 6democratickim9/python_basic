'''
range()함수
'''

print(range(10),range(1,11))
for val in range(1,10,2):
    print(val)

wish_travel_cities = {
    '일본': '도쿄',
    '한국': '서울',
    '프랑스': '파리',
    '미국': '뉴욕'
}

for key in wish_travel_cities.keys():
    print(key)