import binascii
from sha1 import sha1

'''
    Notes:
        - 1 hex string, such as "0xff", is one byte.
        - Message itself is 47 bytes long.
        - HMAC = f4b645e89faaec2ff8e443c595009c16dbdfba4b
        - Message = No one has completed lab 2 so give them all a 0
        - Key length: 128 bits
        - Message length: 47 bytes * 8 = 376 bits
        - K || M = 128 bits + 376 bits = 504
        - First padding = 512 - 504 bits = 8 bits
        - Hacked Message = "Kyle Pontius" =
'''


def get_bit_length(string):
    hex_string = get_hex(string)
    hex_string_length = len(hex_string)
    half_length = hex_string_length // 2
    number_of_bits = half_length * 8

    print "Half Length: {0}".format(half_length)

    return number_of_bits


def get_hex(string):
    return binascii.b2a_hex(string)


if __name__ == '__main__':
    hmac = "f4b645e89faaec2ff8e443c595009c16dbdfba4b"

    hash_result = sha1("Kyle Pontius")
    print "Hash Result: {0}".format(hash_result)

    extension_string = "Kyle Pontius"
    bit_length = get_bit_length(extension_string)


    print "Message length in bits: {0}".format(bit_length)

    hex_version = get_hex(extension_string)
    print "Hex Version: {0}".format(hex_version)