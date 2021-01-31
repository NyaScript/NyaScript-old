from sys import argv
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

inCondition = False
ifAdded = False

inFunction = False
inDefinition = False

inFunction = False
inDefinition = False

CallFunction = ""

tabs = 0

functions = {}

def translate(i, word):
        global inFunction
        global CallFunction
        global inCondition
        global ifAdded
        global script
        global useExtended
        global tabs
        global functions

        writeTabs = ''
        writeTabs = ''.join(["\t" for i in range(tabs)])

        if word == 'OwO':
            useExtended = False
            return ['']

        if word == 'UwU':
            useExtended = True
            return ['']

        elif word == 'Nya':
            return [writeTabs, 'cursor += 1\n']

        elif word == 'nYA':
            tabs -= 1
            return ['']

        elif word == 'nyA':
            return [writeTabs, 'cursor -= 1\n']

        elif word == 'NyA':
            return [writeTabs, 'array[cursor] += 1\n']

        elif word == 'nYa':
            return [writeTabs, 'array[cursor] -= 1\n']

        elif word == 'NYA':
            return [writeTabs, 'print(chr(array[cursor]), end="")\n',]

        elif word == 'nya':
            return [writeTabs, 'array[cursor] = input()\n']
        
        elif word == 'NYa':
            tabs += 1
            return [writeTabs, f'loopCursor[{tabs -1}] = cursor\n',writeTabs, f'while array[loopCursor[{tabs-1}]]:\n']

        elif word == 'nyan':
            return [writeTabs, 'temp =  array[cursor]\n']

        elif word == 'NYAN':
            return [writeTabs, 'array[cursor] = temp\n']
        
        elif word == 'NyaN':
            return [writeTabs, 'temp += 1\n']

        elif word == 'nYAn':
            return [writeTabs, 'temp -= 1\n']

        elif word == 'NYAn':
            return [writeTabs, 'temp += array[cursor]\n']

        elif word == 'nYAN':
            return [writeTabs, 'temp -= array[cursor]\n']

        elif word == 'NyAN':
            return [writeTabs, 'temp = 0\n']

        elif useExtended:

            if word == 'NYA_UwU':
                return [writeTabs, 'print(" ".join(str(array[cursor]).split("\\\\^^")), end="")\n']

            if word.startswith('$'):
                if script[i + 1] == '.':
                    return [writeTabs, f'{word[1:]} = array[cursor]\n']
                elif script[i + 1] == '^':
                    return [writeTabs, f'{word[1:]} = temp\n']
                elif script[i + 1] == '+':
                    return [writeTabs, f'{word[1:]} += array[cursor]\n']
                elif script[i + 1] == '-':
                    return [writeTabs, f'{word[1:]} -= array[cursor]\n']
                else:
                    return [writeTabs, f'{word[1:]} = {script[i + 1]}\n']
            if word.startswith('#'):
                return [writeTabs, f'array[cursor] = {word[1:]}\n']

            if word == 'Nya?':
                tabs += 1
                inCondition = True

            if inCondition:
                if word == 'gweater':
                    if ifAdded:
                        return [writeTabs[1:], 'elif temp > array[cursor]:\n']
                    else:
                        return [writeTabs[1:], 'if temp > array[cursor]:\n']
                elif word == 'lower':
                    if ifAdded:
                        return [writeTabs[1:], 'elif temp < array[cursor]:\n']
                    else:
                        return [writeTabs[1:], 'if temp < array[cursor]:\n']
                if word == 'eqwal':
                    if ifAdded:
                        return [writeTabs[1:], 'elif temp == array[cursor]:\n']
                    else:
                        return [writeTabs[1:], 'if temp == array[cursor]:\n']
            elif word == '?Nya':
                tabs -= 1
                inCondition = False
                return ['']

            if word == 'meow':
                tabs += 1
                funcName = script[i + 1]
                funcArgs = []
                if script[i + 2] == 'meOW':
                    for l in script[i + 3:]:
                        if l != 'MEow':
                            funcArgs.append(l)
                        else:
                            break
                functions.update({funcName: funcArgs})
                return [writeTabs, f"def {funcName}({', '.join(funcArgs)}):\n", writeTabs + '\t',
                        'global array, cursor, temp\n']
            elif word == 'MEOW':
                tabs -= 1
                return ['']

            if word.startswith('~'):
                return [writeTabs, word[1:] + "(" + ', '.join(script[i + 1].split(',')).replace('.', 'array[cursor]')
                .replace('^', 'temp').replace('a', 'int(array[cursor])').replace('t', 'int(temp)') + ")\n"]
                                                                                        
            

            
        return ['']

script_noLines = []
for line in script:
    for word in line:
        script_noLines.append(word)

script = ' '.join(script_noLines).split(' ')
del script_noLines

translated_code = ['array = [0 for i in range(50000)]\n', 'cursor = 0\n', 
                    'loopCursor = [0 for i in range(100)]\n', 'temp = 0\n']

writeTabs = ''

with open(output, "w+") as file:
    i = -1
    for word in script:
        i += 1
        if word == '' or word == None:
            del script[i]
        else:
            writeTabs = ''
            for c in translate(i, word):
                translated_code.append(c)
    translated_code.append('print()')
    file.write(''.join(translated_code))

if execute:
    exec(open(output).read())