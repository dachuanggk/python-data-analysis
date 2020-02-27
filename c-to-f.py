if __name__ == '__main__':
    temp = input('请输入温度')
    if temp[-1] in ['f', 'F']:
        temp_c = (eval(temp[0:-1]) - 32)/1.8
        print(' C=', temp_c)
    elif temp[-1] in ['c', 'C']:
        temp_f = (eval(temp[0:-1]))*1.8 + 32
        print(' f=', temp_f)
    else:
        print('null')
range()