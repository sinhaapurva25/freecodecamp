def exceptionHandling(problems):
    
    if len(problems) > 5:
        raise Exception('Error: Too many problems.')

    for i in problems:
        if i.split()[1] == '+' or i.split()[1] == '-': pass
        else: raise Exception("Error: Operator must be '+' or '-'.")

    numb = ''
    for j in [i.split()[0] for i in problems]+[i.split()[2] for i in problems]:
        numb += j
    for j in numb:
        if j not in '0123456789':
            raise Exception('Error: Numbers must only contain digits.')

    for j in [i.split()[0] for i in problems]+[i.split()[2] for i in problems]:
        if int(j) > 9999:
            raise Exception('Error: Numbers cannot be more than four digits.')

def arithmetic_arranger(problems,resBoolean=False):
    if exceptionHandling(problems):
        return None
    else:
        num1Arr = [int(i.split()[0]) for i in problems]
        operandArr = [i.split()[1] for i in problems]
        num2Arr = [int(i.split()[2]) for i in problems]

        space = '    '
        line1 = ''
        line2 = ''
        line3 = ''
        res = ''

        for idx in range(len(problems)):
            num1 = str(num1Arr[idx])
            num2 = str(num2Arr[idx])
            
            if len(str(num1Arr[idx])) > len(str(num2Arr[idx])):
                num2 = ' '*(len(str(num1Arr[idx])) - len(str(num2Arr[idx]))) + str(num2Arr[idx])
            if len(str(num1Arr[idx])) < len(str(num2Arr[idx])):
                num1 = ' '*(len(str(num2Arr[idx])) - len(str(num1Arr[idx]))) + str(num1Arr[idx])

            line1 += ' '*2 + num1 + space
            line2 += operandArr[idx] + ' ' + num2 + space
            line3 += '-' * len(operandArr[idx] + ' ' + num2) + space

            if resBoolean:
                sum = 0
                if operandArr[idx] == '+':
                    sum = num1Arr[idx] + num2Arr[idx]
                else:
                    sum = num1Arr[idx] - num2Arr[idx]
                res += ' ' * (2 + max(len(str(num1Arr[idx])),len(str(num2Arr[idx]))) - len(str(sum))) + str(sum) + space

        arranged_problems = line1 + '\n' + line2 + '\n' + line3 + '\n' + res
        return arranged_problems