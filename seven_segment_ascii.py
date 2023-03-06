#                                                    .-'''-.                                                     
#                                      .---..---.   '   _    \               .---.                               
#   __  __   ___         __.....__     |   ||   | /   /` '.   \              |   |          /|                   
#  |  |/  `.'   `.   .-''         '.   |   ||   |.   |     \  '       _     _|   |          ||                   
#  |   .-.  .-.   ' /     .-''"'-.  `. |   ||   ||   '      |  '/\    \\   //|   |          ||                   
#  |  |  |  |  |  |/     /________\   \|   ||   |\    \     / / `\\  //\\ // |   |    __    ||  __               
#  |  |  |  |  |  ||                  ||   ||   | `.   ` ..' /    \`//  \'/  |   | .:--.'.  ||/'__ '.       _    
#  |  |  |  |  |  |\    .-------------'|   ||   |    '-...-'`      \|   |/   |   |/ |   \ | |:/`  '. '    .' |   
#  |  |  |  |  |  | \    '-.____...---.|   ||   |                   '        |   |`" __ | | ||     | |   .   | / 
#  |__|  |__|  |__|  `.             .' |   ||   | ________________           |   | .'.''| | ||\    / ' .'.'| |// 
#                      `''-...... -'   '---''---'|________________|          '---'/ /   | |_|/\'..' /.'.'.-'  /  
#                                                                                 \ \._,\ '/'  `'-'` .'   \_.'   
#@Mellow_labs                                                                      `--'  `"
# 7 Segment bit order: DP-G-F-E-D-C-B-A
char_map = {
    ' ': 0b00000000,
    '!': 0b10000110,
    '"': 0b00100010,
    '#': 0b01111110,
    '$': 0b01101101,
    '%': 0b11010010,
    '&': 0b01000110,
    "'": 0b00100000,
    '(': 0b00101001,
    ')': 0b00001011,
    '*': 0b00100001,
    '+': 0b01110000,
    ',': 0b00010000,
    '-': 0b01000000,
    '.': 0b10000000,
    '/': 0b01010010,
    '0': 0b00111111,
    '1': 0b00000110,
    '2': 0b01011011,
    '3': 0b01001111,
    '4': 0b01100110,
    '5': 0b01101101,
    '6': 0b01111101,
    '7': 0b00000111,
    '8': 0b01111111,
    '9': 0b01101111,
    ':': 0b00001001,
    ';': 0b00001101,
    '<': 0b01100001,
    '=': 0b01001000,
    '>': 0b01000011,
    '?': 0b11010011,
    '@': 0b01011111,
    'A': 0b01110111,
    'B': 0b01111100,
    'C': 0b00111001,
    'D': 0b01011110,
    'E': 0b01111001,
    'F': 0b01110001,
    'G': 0b00111101,
    'H': 0b01110110,
    'I': 0b00110000,
    'J': 0b00011110,
    'K': 0b01110101,
    'L': 0b00111000,
    'M': 0b00010101,
    'N': 0b00110111,
    'O': 0b00111111,
    'P': 0b01110011,
    'Q': 0b01101011,
    'R': 0b00110011,
    'S': 0b01101101,
    'T': 0b01111000,
    'U': 0b00111110,
    'V': 0b00111110,
    'W': 0b00101010,
    'X': 0b01110110,
    'Y': 0b01101110,
    'Z': 0b01011011,
    '[': 0b00111001,
    '\\': 0b01100100,
    ']': 0b00001111,
    '^': 0b00100011,
    '_': 0b00001000,
    '`': 0b00000010,
    'a': 0b01011111,
    'b': 0b01111100,
    'c': 0b01011000,
    'd': 0b01011110,
    'e': 0b01111011,
    'f': 0b01110001,
    'g': 0b01101111,
    'h': 0b01110100,
    'i': 0b00010000,
    'j': 0b00001100,
    'k': 0b01110101,
    'l': 0b00110000,
    'm': 0b00010100,
    'n': 0b01010100,
    'o': 0b01011100,
    'p': 0b01110011,
    'q': 0b01100111,
    'r': 0b01010000,
    's': 0b01101101,
    't': 0b01111000,
    'u': 0b00011100,
    'v': 0b00011100,
    'w': 0b00010100,
    'x': 0b01110110,
    'y': 0b01101110,
    'z': 0b01011011,
    '{': 0b01000110,
    '|': 0b00110000,
    '}': 0b01110000,
    '~': 0b00000001
}


def get_char(char):
    return char_map.get(str(char), char_map.get('_'))


def get_char2(char):
    # 7 Segment bit order: DP-A-B-C-D-E-F-G
    bits = get_char(char)
    tmp = '{:08b}'.format(bits)
    return int(''.join(['0b', tmp[0], ''.join(reversed(tmp[1:]))]), 2)


'''
01111001 01101111 01110101 00100000 01100001 01110010 01100101
00100000 01110011 01110101 01100011 01101000 00100000 01100001
00100000 01101110 01100101 01110010 01100100 00100000 01111001
01101111 01110101 00101100 00100000 01101111 01110111 01100101
00100000 01101101 01100101 00100000 00110010 00110000 00100000
01000010 01110101 01100011 01101011 01110011
'''