numStr = input()
for item in range(len(numStr)):
    if numStr[item] == ' ':
        num1 = numStr[0:item]
        oper = numStr[item+1:item+2]
        num2 = numStr[item+2:]
numOper = num1+oper+num2
print("{:.2f}".format(eval(numOper)))
