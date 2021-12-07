strings = []
newline = ''
inp = input("파일이름 입력(.txt 붙여서): ")
path = './' + inp

with open(path, 'r',encoding='utf-8') as text:
    lines = text.readlines()

for i in range(len(lines)):
    lines[i] += '&nbsp;'

for i in range(len(lines)):
    print(lines[i])
        
##except:
##    with open(path, 'r') as text:
##        lines = text.readlines()
##        for t in lines:
##            for c in t:
##                if c not in strings:
##                    strings.append(c)
##                    newline += c
##
##                    
##with open(path, 'w') as text:
##    text.writelines(newline)
