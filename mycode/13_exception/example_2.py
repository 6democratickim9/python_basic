for i in range(10):
    try:
        print(i, 10 // i)
        # 0일 때만 메세지 뿌림
    except ZeroDivisionError as err:
        print(err)
        print("Not divided by 0")
    finally:
        print('END')