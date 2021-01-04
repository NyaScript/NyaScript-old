# NYASCRIPT !!!

script = []

with open("main.bf", "r") as file:
    for line in file:
        for c in line:
            script.append(c)

loop = []

def translate(word):
        if word == '>':
            return 'Nya'

        elif word == ']':
            return 'nYA'

        elif word == '<':
            return 'nyA'

        elif word == '+':
            return 'NyA'

        elif word == '-':
            return 'nYa'

        elif word == '.':
            return 'NYA'
            
        elif word == ',':
            return 'nya'
        
        elif word == '[':
            return 'NYa'

        else:
            return '\n'
            

script_noLines = []
for line in script:
    for word in line:
        
        script_noLines.append(word)

script = ' '.join(script_noLines).split(' ')
del script_noLines

translated_code = []

with open("main.nyas", "w+") as file:
    for i, word in enumerate(script):
        script[i] = word.replace('\n', '')
        script[i] = script[i].replace('\t', '')
        if word == '' or word == '\n' or word == None:
            del script[i]
        if i % 10 == 0:
            translated_code.append('\n')
        translated_code.append(translate(word))
    file.write(' '.join(translated_code))
