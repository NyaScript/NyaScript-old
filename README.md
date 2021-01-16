# NyaScript
A crazy programming language, derivative of Brainfuck

## Installation
Please have python 3 installed
For now, just put the translator.py in your project folder.

## Usage
`python <file.nyas> <options>`

Options: <br>
`-n`: Do not execute after translation <br>
`-o <file.py>`: Sets the output file

## Syntax

Since NyaScript contains a translation of BrainFuck, it works almost like it:

|BF:    |NyaScript:|
|-------|---------|
|>      |Nya      |
|<      |nyA      |
|.      |NYA      |
|,      |nya      |
|[      |NYa      |
|]      |nYA      |
|+      |NyA      |
|-      |nYa      |

But it also has some exclusive features:

|NyaScript:    |Does:|
|-------|---------|
|nyan      |Assigns current matrix pos to temp value      |
|NYAN     |Assigns temp value to current matrix pos     |
|NyaN|Adds one to temp value|
|nYAn|Removes one to temp value|
|NYAn|Adds current matrix pos to temp|
|nYAN|Removes current matrix pos to temp|
|NyAN|Clears temp|