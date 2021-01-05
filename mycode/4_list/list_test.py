'''
list 타입을 선언하고 list 엘리먼트 추가, 삭제 등등
'''
num_list = [10,20,40,40,50]
print(type(num_list),num_list)
print(num_list[0],num_list[0:3])
for idx,num in enumerate(num_list):
    print(idx,num)

str_list = ['python', 'java', 'kotlin', 'C++', 'YOU']
print(type(str_list),str_list)
print(str_list[1],str_list[2:4])

for idx,val in enumerate(str_list):
    print(idx,val)

mix_list = [100,3.14,True,'파이썬']
for mix in mix_list:
    print(type(mix),mix)