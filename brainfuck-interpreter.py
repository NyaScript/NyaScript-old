import brainfuck

bf = ''

with open('main.bf') as file:
    for line in file:
        bf += line


print(brainfuck.evaluate(bf))
