result = []
for val in range(10):
    if val % 2 == 0:
        result.append(val)


print(result)
#밑에가 리스트 컴프리헨션
result2 = [val for val in range(10)]
print(result2)

my_str1 = "Hello"
my_str2 = "World"

result = [i+j for i in my_str1 for j in my_str2 if not (i==j)]
print(result)