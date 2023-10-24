def func(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


func(1, 2, 3, 4, key1="value1", key2="value2")