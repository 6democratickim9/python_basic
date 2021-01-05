def add(x,y):
    return x+y


print(add(1,4))

add2 = lambda x, y : x + y
print(add2(10,20))

print((lambda x,y: x+y)(10,20))

print((lambda x:x ** 2)(10))


f= lambda x,y: x+y
print(f(1,4))

f= lambda x:x/2
print(f(3))
print((lambda x:x+1)(5))

#map(함수,list)함수
double_val = lambda x: x**2
print(double_val(2))

my_list = [1,2,3,4,5]
#for loop 사용해서 함수호출
result_list = []
for val in my_list:
    print(double_val(val))
    result_list.append(double_val(val))

print(result_list)

result = map(double_val,my_list)
print(type(result), result)
result = list(map(double_val,my_list))
print(result)

result = list(map(lambda x: x ** 2, my_list))
print(result)
list_one=[1,2,3,4,5]
list_two=[10,20,30,40,50]
#리스트_1,2 더하기
result1= list(map(lambda x,y:x+y,list_two,list_one))
print(result1)

add = lambda x,y : x+y
print(add(1,10))
result = list(map(add, list_one,list_two))
print(result)

#짝수만 제곱하는 함수
double_even = lambda x: x**2 if x % 2 == 0 else x
print(double_even(4),double_even(5))
print(list(map(double_even,list_one)))
print(list(map(lambda x: x**2 if x % 2 == 0 else x,list_one)))

#for문돌리기
for val in map(double_even,list_one):
    print(val)

map_obj= map(double_even,list_one)
print(next(map_obj),next(map_obj))


'''
reduce()함수
'''
from functools import reduce

add = lambda x,y: x + y
print(add(1,4))

result = reduce(add, list_one)
print(result)
result = reduce(lambda prev, curr: prev + curr, my_list)
print(result)

result_str = reduce(lambda prev, curr: prev + curr, ['aa','bb','cc'])
print(result_str)

'''
filter 함수
'''
my_len = lambda my_str: len(my_str) > 6
print(my_len('hello'))

my_list_str = ['mython', 'python', 'onenight','lullaby', 'bye']
result=filter(my_len, my_list_str)
print(type(result))
