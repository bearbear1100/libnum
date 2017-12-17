#-*- coding:utf-8 -*-
from binascii import unhexlify

def s2n(s):
    """
    String to number.
    """
    if not len(s):
        return 0
    if type(s) == str :
        return int(''.join( hex(ord(c))[2:].rjust(2,'0') for c in s),16)
    if type(s) == bytes :
        return int.from_bytes(s,'big')


def n2s(n,byteorder='big'):
    """
    Number to string.
    """
    length = (len(hex(n))-1)//2
    return int(n).to_bytes(length=length,byteorder=byteorder)


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
