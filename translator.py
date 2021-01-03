# NYASCRIPT !!!

script = []

with open("main.nyas", "r") as file:
    for line in file:
        script.append(line.split(" "))
    for index, line in enumerate(script):
        for i, nya in enumerate(line):
            script[index][i] = nya.replace("\n", '')
            if script[index][i] == '':
                del script[index][i]
loop = []

tabs = 0

def translate(word):
        global tabs
        if word == 'Nya':
            return 'cursor += 1\n'

        elif word == 'nYA':
            tabs -= 1
            return '\n'

        elif word == 'nyA':
            return 'cursor -= 1\n'

        elif word == 'NyA':
            return 'array[cursor] += 1\n'

        elif word == 'nYa':
            return 'array[cursor] -= 1\n'

        elif word == 'NYA':
            return 'print(chr(array[cursor]), end="")\n'
            
        elif word == 'nya':
            return 'inpt = input()\nif inpt:\n\tarray[cursor] = ord(inpt[0])\n'
        
        elif word == 'NYa':
            tabs += 1
            return f'loopCursor[{tabs - 1}] = int(str(cursor))\nwhile array[loopCursor[{tabs -1}]]:\n'

        else:
            return '\n'
            

script_noLines = []
for line in script:
    for word in line:
        
        script_noLines.append(word)

script = ' '.join(script_noLines).split(' ')
del script_noLines

translated_code = ['array = [0 for i in range(50000)]\n', 'cursor = 0\n', 'loopCursor = [0]\n']
looping = False

with open("main.py", "w+") as file:
    for i, word in enumerate(script):
        script[i] = word.replace('\n', '')
        script[i] = script[i].replace('\t', '')
        if word == '' or word == None:
            del script[i]
        writeTabs = ''
        for i in range(tabs):
            writeTabs += '\t'
        translated_code.append(writeTabs + translate(word))
    translated_code.append('print()')
    file.write(''.join(translated_code))
