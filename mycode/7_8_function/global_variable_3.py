
def kwargs_dict(**p):
    print(p,type(p))
    for k, v in p.items():
         print(k,v)


print(kwargs_dict(a=100,b=100,c=100))
