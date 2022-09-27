from os import system

MORSE = '".-"-..."-.-."-.."."..-."--."...."..".---"-.-".-.."--"-."---' \
        '".--."--.-".-."..."-"..-"...-".--"-..-"-.--"--.."' \
        '..--"-.-.--"..--..".-.-.-"--..--'
MORSECHAR = MORSE.split('"')

ROMANIC = '~"a"b"c"d"e"f"g"h"i"j"k"l"m"n"o"p"q"r"s"t"u"v"w"x"y"z' \
          '" "!"?".",'
ROMANICCHAR = ROMANIC.split('"')


def romanify(txt):
    res = str()
    letters = txt.split(' ')

    for index, morse_letter in enumerate(letters):  # Search for every typed letter

        # Check the letter's positions.
        for position, searched_letter in enumerate(MORSECHAR):
            if morse_letter == searched_letter:
                res += ROMANICCHAR[position]

    return res


def morsefy(txt):
    res = str()

    for letter in txt:
        index = ROMANICCHAR.index(letter)
        res += MORSECHAR[index] + ' '

    return res


def title():
    print(f'{"MORSE":^50}\n'
          f'{"&":^50}\n'
          f'{"ROMANIC":^50}\n'
          f'{"=" * 50}\n'
          f'Type "$help" for help')


def functions(cmd):

    if cmd.lower() == '$help':
        print(f'You can type in using romanic letters or morse code. If you type in romanic, it will translate\n'
              f'to morse code and vice versa.\n'
              f'\n'
              f'{"FUNCTIONS":^30}\n'
              f'CLEAR: {"_" * 16} $clear')

    if cmd.lower() == '$clear':
        system('clear')
        title()



