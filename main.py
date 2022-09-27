from logic import morsefy, romanify, functions, title

title()
while True:
    txt = input('>>> ')
    if txt[0] == '$':
        functions(txt)

    elif txt[0] == '.' or txt[0] == '-':
        print(romanify(txt))

    else:
        print(morsefy(txt))
