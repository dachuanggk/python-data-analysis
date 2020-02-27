numStr = input('请输入一个整数')
num = eval(numStr)
printStr = 'Hello World'
if num == 0:
    print(printStr)
elif num > 0:
    for item in range(0, len(printStr), 2):
        print(printStr[item:item+2])
elif num < 0:
    for item in range(len(printStr)):
        print(printStr[item:item+1])
else:
    print('请输入整数')
