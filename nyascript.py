from sys import argv, executable
import os

# NYASCRIPT !!!

useExtended = False

execute = True
src = None
output = None

script = []
argc = len(argv)

if not argc:
    print("ERROR: No filename given")
    exit()
elif argc == 1:
    pass

for arg in argv:
    if arg == '-n':
        execute = False
    if arg == '-o':
        output = os.path.join(os.curdir, argv[argv.index(arg) + 1])
if not output:
    output = os.path.join(os.curdir, 'main.py')

src = os.path.join(os.curdir, argv[1])

with open(src, "r") as file:
    for line in file:
        script.append(line.split(" "))
    for index, line in enumerate(script):
        for i, nya in enumerate(line):
            script[index][i] = nya.replace("\n", '')
            if script[index][i] == '':
                del script[index][i]

loop = []

tabs = 0

variables = {}

def translate(i, word):
        global script
        global useExtended
        global variables
        global tabs

        if word == 'OwO':
            useExtended = False
            return ['']

        if word == 'UwU':
            useExtended = True
            return ['']

        elif word == 'Nya':
            return ['cursor += 1\n']

        elif word == 'nYA':
            tabs -= 1
            return ['\n']

        elif word == 'nyA':
            return ['cursor -= 1\n']

        elif word == 'NyA':
            return ['array[cursor] += 1\n']

        elif word == 'nYa':
            return ['array[cursor] -= 1\n']

        elif word == 'NYA':
            return ['print(chr(array[cursor]), end="")\n']
            
        elif word == 'nya':
            return ['inpt = input()\nif inpt:\n\tarray[cursor] = ord(inpt[0])\n']
        
        elif word == 'NYa':
            tabs += 1
            return [f'loopCursor[{tabs - 1}] = int(str(cursor))\n',f'while array[loopCursor[{tabs -1}]]:\n']

        elif word == 'nyan':
            return ['temp = int(str(array[cursor]))\n']

        elif word == 'NYAN':
            return ['array[cursor] = int(str(temp))\n']
        
        elif word == 'NyaN':
            return ['temp += 1\n']

        elif word == 'nYAn':
            return ['temp -= 1\n']

        elif word == 'NYAn':
            return ['temp += int(str(array[cursor]))\n']

        elif word == 'nYAN':
            return ['temp -= int(str(array[cursor]))\n']

        elif word == 'NyAN':
            return ['temp = 0\n']

        elif useExtended:
            if word.startswith('$'):
                if not variables.get(word[1:]) and not variables.get(word[1:]) == 0:
                    variables.update({word[1:]: 0})
                    return [f'{word[1:]} = 0\n']
                elif variables.get(word[1:]) or variables.get(word[1:]) == 0:
                    variables.update({word[1:]: script[i + 1]})
                    if script[i + 1] == '.':
                        return [f'{word[1:]} = array[cursor]\n']
                    elif script[i + 1] == '^':
                        return [f'{word[1:]} = temp\n']
                    elif script[i + 1] == '+':
                        return [f'{word[1:]} += array[cursor]\n']
                    elif script[i + 1] == '-':
                        return [f'{word[1:]} -= array[cursor]\n']
                    else:
                        return [f'{word[1:]} = int({script[i + 1]})\n']
                else:
                    return ['print("LOL")\n']
            if word.startswith('#'):
                if not variables.get(word[1:]) and not variables.get(word[1:]) == 0:
                    return ['print(ERROR: NO VARIABLES TO CALL UwU)']
                elif variables.get(word[1:]) or variables.get(word[1:]) == 0:
                    return [f'array[cursor] = int(str({word[1:]}))\n']
        return ['']

script_noLines = []
for line in script:
    for word in line:
        script_noLines.append(word)

script = ' '.join(script_noLines).split(' ')
del script_noLines

translated_code = ['array = [0 for i in range(50000)]\n', 'cursor = 0\n', 
                    'loopCursor = [0]\n', 'temp = 0\n']

with open(output, "w+") as file:
    i = -1
    for word in script:
        i += 1
        script[i] = word.replace('\n', '')
        script[i] = script[i].replace('\t', '')
        if word == '' or word == None:
            del script[i]
        writeTabs = ''
        for i in range(tabs):
            writeTabs += '\t'
        for c in translate(i, word):
            translated_code.append(writeTabs + c)
    translated_code.append('print()')
    file.write(''.join(translated_code))

if execute:
    os.system(f'{os.path.dirname(executable)}\\python {output}')
