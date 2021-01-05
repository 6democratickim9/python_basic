words = 'Arguments are made by me and you so we should solve it'.split()
print(words)

my_list = [[w.upper(),w.lower(),w.title(), len(w)] for w in words]
print(type(my_list),my_list)
for word in my_list:
    print(word)

for idx,w in enumerate(words):
    print(idx,w)

print(enumerate(words),type(enumerate(words)))
print(list(enumerate(words)))

word_dict = {idx:w for idx, w in enumerate(words,1)}
print(word_dict)

my_list = [1,2,3]
my_list2 = [10,20,30]
my_list3= [100,200,300]

print(zip(my_list,my_list2,my_list3),type(zip(my_list,my_list2,my_list3)))
print(list(zip(my_list,my_list2,my_list3)))

for val in zip(my_list,my_list2,my_list3):
    print(type(val),val,sum(val))

result= [sum(val) for val in zip(my_list,my_list2,my_list3)]
print(result)

result_dict = {idx:sum(val) for idx,val in enumerate(zip(my_list,my_list2,my_list3))}
print(result_dict)


a,b,c=zip(my_list,my_list2,my_list3)
print(a,b,c)