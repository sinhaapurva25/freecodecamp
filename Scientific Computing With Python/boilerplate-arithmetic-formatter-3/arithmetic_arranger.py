def arithmetic_arranger(problems,*args):
    space = '    '
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''

    if len(problems) > 5:
        raise Exception('Error: Too many problems')

    for i in problems:
        i = i.strip()
        # print("i.strip()",i)
        if i.find('*') > 0 or i.find('/') > 0:
            raise Exception("Error: Operator must be '+' or '-'")
        for k in i:
            if ((k >= 'a' and k <= 'z') or (k >= 'A' and k <= 'Z')):
                raise Exception("Error: Numbers must only contain digits")
        k = i.find('+') + i.find('-')

        element1 = int(i[:k])
        element2 = int(i[k + 3:])

        if (element1 > 9999) or (element2 > 9999):
            raise Exception("Error: Numbers cannot be more than four digits")
        str_element1 = i[:k]
        str_element2 = i[k + 3:]

        len_el_1 = len(str_element1)
        len_el_2 = len(str_element2)

        if (len_el_1 == len_el_2):
            indent_len = 0
            line1 = line1 + '  ' + str_element1 + space
            line2 = line2 + i[k + 1] + ' ' + str_element2 + space
            dash_length = len(i[k + 1] + ' ' + str_element2)
            dash = ''
            for d in range(0, dash_length):
                dash = dash + '-'
            line3 = line3 + dash + space
        elif (len_el_1 > len_el_2):
            indent_len = (len_el_1 - len_el_2)
            indent = ''
            for d in range(0, indent_len):
                indent = indent + ' '
            line1 = line1 + '  ' + str_element1 + space
            line2 = line2 + i[k + 1] + ' ' + indent + str_element2 + space
            dash_length = len(i[k + 1] + '' + str_element1)
            dash = ''
            for d in range(0, dash_length + 1):
                dash = dash + '-'
            line3 = line3 + dash + space
        else:
            indent_len = (len_el_2 - len_el_1)
            indent = ''
            for d in range(0, indent_len):
                indent = indent + ' '
            line1 = line1 + '  ' + indent + str_element1 + space
            line2 = line2 + i[k + 1] + ' ' + str_element2 + space
            dash_length = len(i[k + 1] + '' + str_element2)
            dash = ''
            for d in range(0, dash_length + 1):
                dash = dash + '-'
            line3 = line3 + dash + space

        for a in args:
            if a:
                if i[k + 1] == '+':
                    sum = element1 + element2
                else:
                    sum = element1 - element2
                str_sum = str(sum)
                indent_len_dash = abs(max(len_el_1, len_el_2) - len(
                    str_sum)) + 2  # adding one space for operand and another for the pace between the second operant and operand
                indent = ''
                for d in range(0, indent_len_dash):
                    indent = indent + ' '
                line4 = line4 + indent + str_sum + space
    arranged_problems = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    return arranged_problems