#-*- coding:utf-8 -*-

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
    if type(s) == type(b''):
        s = "".join(map(chr, s))
    for c in s:
        ret.append(bin(ord(c))[2:].zfill(8))
    return "".join(ret)

def switchBS(bs):
    """
    Switch bytes and string.
    """
    if type(bs) == type(b''):
        return "".join(map(chr, bs))
    return n2s(int(''.join( hex(ord(c))[2:].rjust(2,'0') for c in bs),16))
    

def b2s(b):
    """
    Binary to string.
    """
    ret = []
    if type(s) == type(b''):
        b = switchBS(b)
    for pos in range(0, len(b), 8):
        ret.append(chr(int(b[pos:pos + 8], 2)))
    return ''.join(ret)


