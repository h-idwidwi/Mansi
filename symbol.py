output_text = []
with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    for char in text:
        if ord(char) == 0xF50E:
            char = 'А̄'
        elif ord(char) == 0xF50F:
            char = 'а̄'
        elif ord(char) == 0x0101:
            char = 'а̄'
        elif ord(char) == 0xF511:
            char = '\u0113'
        elif ord(char) == 0x0113:
            char = '\u0113'
        elif ord(char) == 0xF52C:
            char = 'Ю̄'
        elif ord(char) == 0xF52D:
            char = 'ю̄'
        elif ord(char) == 0xF518:
            char = 'О̄'
        elif ord(char) == 0xF519:
            char = 'о̄'
        elif ord(char) == 0x014D:
            char = 'о̄'
        elif ord(char) == 0xF522:
            char = 'Э̄'
        elif ord(char) == 0xF523:
            char = 'э̄'
        elif ord(char) == 0xF512:
            char = 'Ё̄'
        elif ord(char) == 0xF513:
            char = 'ё̄'
        elif ord(char) == 0xF528:
            char = 'Я̄'
        elif ord(char) == 0xF529:
            char = 'я̄'
        elif ord(char) == 0x04EF:
            char = 'ӯ'
        elif ord(char) == 0xF521:
            char = 'ы̄'
        
        output_text.append(char)

output_text = ''.join(output_text)

with open('text.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(output_text)
