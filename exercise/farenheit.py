def fah_convert(value):
    return ((9/5)*float(value))+32

print("변환할 섭씨 온도")


user_input = input()

result = fah_convert(user_input)


print("섭씨 ", user_input)
print("화씨 ", round(result,2))
print("화씨 {:.2f}".format(result))

def sayHello(msg):
    return f'Hello {msg}!'