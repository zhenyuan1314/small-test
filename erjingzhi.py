try:
    def zhuan(x):
        result = []
        while x:        
            a = x // 2
            t = x % 2
            x = a
            result.append(t)
        result.reverse()
        for each in result:
            print(each , end = '')
    temp = input('请输入要转换成二进制的数字：')
    x = int (temp)
    zhuan(x)

except TypeError as reason:
    print('类型出错的原因' + str(reason))

