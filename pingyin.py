#输入0-9，输出数字拼音，用空格隔开
a = input()
ans = []
for i in a:
    if i == '1':
        ans.append('yi')
    elif i == '2':
        ans.append('er')
    elif i == '3':
        ans.append('san')
    elif i == '4':
        ans.append('si')
    elif i == '5':
        ans.append('wu')
    elif i == '6':
        ans.append('liu')
    elif i == '7':
        ans.append('qi')
    elif i == '8':
        ans.append('ba')
    elif i == '9':
        ans.append('jiu')
    elif i == '0':
        ans.append('ling')
    elif i == '-':
        ans.append('-')
for i in ans:
    print(i,end=' ')