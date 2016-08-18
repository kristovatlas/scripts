"""How many different characters are in the input string?"""

import sys
import math

def _main():
    if len(sys.argv) != 2:
        sys.exit("Wrong number of args")

    charset = set(str(sys.argv[1]))
    print "There are %d characters: '%s'" % (len(charset), 
                                             _sorted_str_of_set(charset))
    power = _power_of_dos(len(charset))
    if power is not None:
        bits = len(sys.argv[1]) * power
        print "There is exactly %d bits of data encoded in this string." % bits

def _power_of_dos(num):
    """ Get the exponent of two which matches the number
    http://stackoverflow.com/questions/15352593/how-to-check-if-a-number-is-a-power-of-base-b#15352628
    """
    power = int(math.log(num, 2) + 0.5)
    if (2**power) == num:
        return power
    else:
        return None

def _sorted_str_of_set(data):
    return ''.join(sorted(data, key=lambda item:
                          (int(item.partition(' ')[0])
                           if item[0].isdigit() else float('inf'), item)))

if __name__ == '__main__':
    _main()
