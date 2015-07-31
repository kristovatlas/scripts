#!/usr/bin/python
# Generate a random string of UTF-8 characters

#https://en.wikipedia.org/wiki/Unicode_control_characters
#banned characters:  U+0000 - U+0020, U+007F, U+0080 - U+009F, U+2028, U+2029, U+200E, U+200F, U+202A - U+202E

import random

banned_chars = [range(0x0000, 0x0020),
    range(0x007f, 0x007f),
    range(0x0080, 0x009f),
    range(0x2028, 0x2029),
    range(0x200e, 0x200f),
    range(0x202a, 0x202e)]

#http://stackoverflow.com/questions/1477294/generate-random-utf-8-string-in-python
def get_random_unicode(length):

    try:
        get_char = unichr
    except NameError:
        get_char = chr

    # Update this to include code point ranges to be sampled
    include_ranges = [
        ( 0x0021, 0x0021 ),
        ( 0x0023, 0x0026 ),
        ( 0x0028, 0x007E ),
        ( 0x00A1, 0x00AC ),
        ( 0x00AE, 0x00FF ),
        ( 0x0100, 0x017F ),
        ( 0x0180, 0x024F ),
        ( 0x2C60, 0x2C7F ),
        ( 0x16A0, 0x16F0 ),
        ( 0x0370, 0x0377 ),
        ( 0x037A, 0x037E ),
        ( 0x0384, 0x038A ),
        ( 0x038C, 0x038C ),
    ]

    alphabet = [
        get_char(code_point) for current_range in include_ranges
            for code_point in range(current_range[0], current_range[1] + 1)
    ]
    return ''.join(random.choice(alphabet) for i in range(length))

def get_unbanned_random_unicode(length):
    ret = ''
    for i in xrange(length):
        while True:
            char = get_random_unicode(1)
            #print("%s" % hex(ord(char)))
            #print("%s" % char)
            banned = False
            for banned_range in banned_chars:
                if ord(char) in banned_range:
                    #print("banned")
                    banned = True
                    break
            if not banned:
                ret = ret + char
                break
    return ret

if __name__ == '__main__':
    print(get_unbanned_random_unicode(4))
