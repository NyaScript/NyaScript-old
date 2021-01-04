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

def translate(word):
        if word == 'Nya':
            return '>'

        elif word == 'nYA':
            return ']'

        elif word == 'nyA':
            return '<'

        elif word == 'NyA':
            return '+'

        elif word == 'nYa':
            return '-'

        elif word == 'NYA':
            return '.'
            
        elif word == 'nya':
            return ','
        
        elif word == 'NYa':
            return '['

        else:
            return '\n'
            

script_noLines = []
for line in script:
    for word in line:
        
        script_noLines.append(word)

script = ' '.join(script_noLines).split(' ')
del script_noLines

translated_code = []

with open("main.bf", "w+") as file:
    for i, word in enumerate(script):
        script[i] = word.replace('\n', '')
        script[i] = script[i].replace('\t', '')
        if word == '' or word == None:
            del script[i]
        if script % 10 == 0:
            translated_code.append('\n')
        translated_code.append(translate(word))
    file.write(''.join(translated_code))
