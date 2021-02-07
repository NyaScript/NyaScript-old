from sys import argv
import os
import json

# NYASCRIPT !!!

config = json.load(open('config/config.json'))
compileOptions = config['compile_options']

usePlusPlus = False
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
inClass = False
inDefinition = False

tabs = 0

def translate(i, word, script, prefix=''):
        global inFunction, inClass
        global inCondition, ifAdded
        global tabs
        global useExtended, usePlusPlus

        writeTabs = ''
        writeTabs = ''.join(["\t" for i in range(tabs)])

        if word == 'OwO':
            usePlusPlus = True
            return ['']

        if word == 'UwU':
            useExtended = True
            return ['']

        elif word == 'Nya':
            return [writeTabs, f'{prefix}cursor += 1\n']

        elif word == 'nYA':
            tabs -= 1
            return ['']

        elif word == 'nyA':
            return [writeTabs, f'{prefix}cursor -= 1\n']

        elif word == 'NyA':
            return [writeTabs, f'{prefix}array[cursor] += 1\n']

        elif word == 'nYa':
            return [writeTabs, f'{prefix}array[cursor] -= 1\n']

        elif word == 'NYA':
            return [writeTabs, f'print(chr(array[{prefix}cursor]), end="")\n',]

        elif word == 'nya':
            return [writeTabs, f'{prefix}array[{prefix}cursor] = ord(input()[0])\n']
        
        elif word == 'NYa':
            tabs += 1
            return [writeTabs, f'{prefix}loopCursor[{tabs -1}] = {prefix}cursor\n',writeTabs, f'while {prefix}array[{prefix}loopCursor[{tabs-1}]]:\n']

        elif word == 'nyan':
            return [writeTabs, f'{prefix}temp = {prefix}array[{prefix}cursor]\n']

        elif word == 'NYAN':
            return [writeTabs, f'{prefix}array[{prefix}cursor] = {prefix}temp\n']
        
        elif word == 'NyaN':
            return [writeTabs, f'{prefix}temp += 1\n']

        elif word == 'nYAn':
            return [writeTabs, f'{prefix}temp -= 1\n']

        elif word == 'NYAn':
            return [writeTabs, f'{prefix}temp += {prefix}array[{prefix}cursor]\n']

        elif word == 'nYAN':
            return [writeTabs, f'{prefix}temp -= {prefix}array[{prefix}cursor]\n']

        elif word == 'NyAN':
            return [writeTabs, f'{prefix}temp = 0\n']

        if useExtended:
            if word == 'NYA+':
                return [writeTabs, f'print(" ".join(str({prefix}array[{prefix}cursor]).split("\\\\^^")), end="")\n']
            if word == 'nya+':
                return [writeTabs, f'{prefix}array[{prefix}cursor] = input()\n']
            if word.startswith('$') and not word.startswith('$->'):
                try:
                    if usePlusPlus:
                        if script[i + 1] == '^array':
                            array = []
                            for l in script[i + 2:]:
                                if l != 'array^':
                                    array.append(l)
                                else:
                                    break
                            return [writeTabs, f'{word[1:]} = {array}\n']
                        if script[i + 1].startswith('<') and script[i + 1].endswith('>'):
                            return [writeTabs, f'{word[1:]} = {script[i + 1][1:-1]}({script[i + 2]})\n']
                        elif script[i + 1] == '^+':
                            return [writeTabs, f'{word[1:]}.append{array[i + 2]}']
                    if script[i + 1] == '.':
                        return [writeTabs, f'{word[1:]} = {prefix}array[{prefix}cursor]\n']
                    elif script[i + 1] == '^':
                        return [writeTabs, f'{word[1:]} = {prefix}temp\n']
                    elif script[i + 1] == '+':
                        return [writeTabs, f'{word[1:]} += {prefix}array[{prefix}cursor]\n']
                    elif script[i + 1] == '-':
                        return [writeTabs, f'{word[1:]} -= {prefix}array[{prefix}cursor]\n']
                    else:
                        return [writeTabs, f'{word[1:]} = {script[i + 1]}\n']
                except IndexError:
                    return ['']
            if word.startswith('#') and not word.startswith('#->'):
                return [writeTabs, f'{prefix}array[{prefix}cursor] = {word[1:]}\n']

            if word == 'Nya?':
                tabs += 1
                inCondition = True

            if inCondition:
                if word == 'gweater':
                    if ifAdded:
                        return [writeTabs[1:], f'elif {prefix}temp > {prefix}array[{prefix}cursor]:\n']
                    else:
                        return [writeTabs[1:], f'if {prefix}temp > {prefix}array[{prefix}cursor]:\n']
                elif word == 'lower':
                    if ifAdded:
                        return [writeTabs[1:], f'elif {prefix}temp < {prefix}array[{prefix}cursor]:\n']
                    else:
                        return [writeTabs[1:], f'if {prefix}temp < {prefix}array[{prefix}cursor]:\n']
                if word == 'eqwal':
                    if ifAdded:
                        return [writeTabs[1:], f'elif {prefix}temp == {prefix}array[{prefix}cursor]:\n']
                    else:
                        return [writeTabs[1:], f'if {prefix}temp == {prefix}array[{prefix}cursor]:\n']
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
                if usePlusPlus:
                    if funcName == 'constructor':
                        return [writeTabs, f"def __init__(self, {', '.join(funcArgs)}):\n"]
                    else:
                        return [writeTabs, f"def {funcName}(self, {', '.join(funcArgs)}):\n", writeTabs + '\t',
                            f'global {prefix}array, {prefix}cursor, {prefix}temp\n']
                return [writeTabs, f"def {funcName}({', '.join(funcArgs)}):\n", writeTabs + '\t',
                        f'global {prefix}array, {prefix}cursor, {prefix}temp\n']
            elif word == 'MEOW':
                tabs -= 1
                return ['']

            if word.startswith('~'):
                try:
                    if script[i + 2].startswith('°'):
                        return [writeTabs, word[1:] + "(" + ', '.join(script[i + 1].split(',')).replace('.', f'{prefix}array[{prefix}cursor]')
                    .replace('^', f'{prefix}temp').replace('a', f'int({prefix}array[{prefix}cursor])').replace('t', f'int({prefix}temp)') + ")\n"]
                    else:
                        return [writeTabs,f'{word[2:]}.{script[i + 1][1:]}()\n']
                except IndexError:
                    return [writeTabs, word[1:] + "()\n"]


        if usePlusPlus:
            if word == 'hewo!':
                return [writeTabs, f'from {script[i + 1]} import *\n']
            if word == "hewo":
                return [writeTabs, compileDependency(script[i + 1], 'c')]
            
            if word == 'pywon':
                return [writeTabs, f'exec(open("{script[i + 1]}").read())\n']

            if word == 'ewawuate':
                return compileDependency(script[i + 1], 'e')
            
            if word == 'NYA++':
                return [writeTabs, f'print(" ".join({script[i + 1]}.split("\^^")), end="")\n']

            if word == 'Cwass':
                inClass = True
                tabs += 1
                if script[i + 2] == 'extends':
                    return [writeTabs, f'class {script[i + 1]}({script[i + 3]}):\n']
                else:
                    return [writeTabs, f'class {script[i + 1]}:\n']
            if word == 'upper':
                return [writeTabs, "super" + "(" + ', '.join(script[i + 1].split(',')).replace('.', f'{prefix}array[{prefix}cursor]')
                    .replace('^', f'{prefix}temp').replace('a', f'int({prefix}array[{prefix}cursor])').replace('t', f'int({prefix}temp)') + ")\n"]

            if word == '!':
                inClass = False
                tabs -= 1
                return ['']
            
            if word.startswith('$->') and inClass:
                return [writeTabs, f'self.{word[3:]} = {script[i + 1]}\n']
            if word.startswith('#->') and inClass:
                return [writeTabs, f'{prefix}array[{prefix}cursor] = self.{word[3:]}\n']

            if word.startswith('->'):
                if script[i + 1].startswith("/"):
                    try:
                        if script[i + 2].startswith('°'):
                            return [writeTabs,f'{word[2:]}.{script[i + 1][1:]}({script[i + 2]})\n']
                        else:
                            return [writeTabs,f'{word[2:]}.{script[i + 1][1:]}()\n']
                    except IndexError:
                        return [writeTabs,f'{word[2:]}.{script[i + 1][1:]}()\n']
                if script[i + 1].startswith("$->"):
                    return [writeTabs, f'{word[2:]}.{script[i + 1][3:]} = {script[i + 2]}\n']
                if script[i + 1].startswith("#->"):
                    return [writeTabs, f'{prefix}array[{prefix}cursor] = {word[2:]}.{script[i + 1][3:]}\n']
                

        return ['']

def compileDependency(filename, type_):
    dep = []
    build= []
    with open(config["import_folder"] + filename, 'r') as file:
        for line in file:
            dep.append(line.split(" "))
                
    dep_noLines = []
    for line in dep:
        for i, word in enumerate(line):
            if word == '':
                    del dep[i]
    for line in dep:
        for i, word in enumerate(line):
            word = word.replace("\n", '')
            if not word == '':
                dep_noLines.append(word)

    dep = ' '.join(dep_noLines).split(' ')
    del dep_noLines

    if type_ == 'c':
        build = [f'{filename[:-5]}_array = [0 for i in range(50000)]\n', f'{filename[:-5]}_cursor = 0\n', 
        f'{filename[:-5]}_loopCursor = [0 for i in range(100)]\n', f'{filename[:-5]}_temp = 0\n']
        for i, word in enumerate(dep):
            for c in translate(i, word, dep, filename[:-5] + '_'):
                build.append(c)
        with open(config["distributable_folder"] + filename[:-5] + '.py', 'w+') as file:
            file.write(''.join(build))
        return f'from {filename[:-5]} import *\n' 
    elif type_ == 'e':
        for i, word in enumerate(dep):
            for c in translate(i, word, dep):
                build.append(c)
        return build

script_noLines = []
for line in script:
    for word in line:
        script_noLines.append(word)

script = ' '.join(script_noLines).split(' ')
del script_noLines

translated_code = [f'import sys \nsys.path.append("{config["distributable_folder"]}")\n', f'array = [0 for i in range({compileOptions["array_size"]})]\n', f'cursor = {compileOptions["begin_pos"]}\n', 
                    f'loopCursor = [0 for i in range({compileOptions["loopCursor_size"]})]\n', 'temp = 0\n']

writeTabs = ''

with open(output, "w+") as file:
    i = -1
    for word in script:
        i += 1
        if word == '' or word == None:
            del script[i]
        else:
            writeTabs = ''
            for c in translate(i, word, script):
                translated_code.append(c)
    translated_code.append('print()')
    file.write(''.join(translated_code))

if execute:
    exec(open(output).read())