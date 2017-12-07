#-*- coding:utf-8 -*-
from binascii import unhexlify

def s2n(s):
    """
    String to number.
    """
    if not len(s):
        return 0
    return int(''.join( hex(ord(c))[2:].rjust(2,'0') for c in test),16)


def n2s(n):
    """
    Number to string.
    """
    s = hex(n)[2:]
    if len(s) % 2 != 0:
        s = "0" + s
    return "".join([s[i:i+2] for i in range(0, len(s), 2)])


def s2b(s):
    """
    String to binary.
    """
    ret = []
    for c in s:
        ret.append(bin(ord(c))[2:].zfill(8))
    return "".join(ret)


def b2s(b):
    """
    Binary to string.
    """
    ret = []
    for pos in range(0, len(b), 8):
        ret.append(chr(int(b[pos:pos + 8], 2)))
    return "".join(ret)
