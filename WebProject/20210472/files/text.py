strings = []
newline = ''
inp = input("파일이름 입력(.txt 붙여서): ")
path = './' + inp

with open(path, 'r',encoding='utf-8') as text:
    lines = text.readlines()

for line in lines:
    if line != '<br>>>>\n':
        line = line.replace('    ', '&emsp;')
        line = line.replace('	', '&emsp;')
        line = line.replace('<br>', '')
        line += '<br>'
        newline += line
    else:
        newline += '>>>'
        print("!")

        
                    
with open(path, 'w', encoding="utf-8") as text:
    text.writelines(newline)
