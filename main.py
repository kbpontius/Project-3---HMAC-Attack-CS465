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
        - K || M = 128 bits + 376 bits = 504 bits
        - First padding => 512 - 504 bits = 8 bits
        - Hacked Message => "PS Kyle Pontius should get full points." = 96 bits
'''


def get_bit_length(string):
    hex_string = get_hex(string)
    hex_string_length = len(hex_string)
    half_length = hex_string_length // 2
    number_of_bits = half_length * 8

    return number_of_bits


def get_hex(string):
    return binascii.b2a_hex(string)


if __name__ == '__main__':
    original_hmac = "f4b645e89faaec2ff8e443c595009c16dbdfba4b"
    original_message = "No one has completed lab 2 so give them all a 0"
    # original_padding = "1"
    hacked_message = "PS Kyle Pontius should get full points."

    original_message_hex = get_hex(original_message)
    print "Original message hex: {0}".format(original_message_hex)

    original_message_bit_length = get_bit_length(original_message)
    print "Original message bit length: {0}".format(original_message_bit_length)

    hacked_bit_length = get_bit_length(hacked_message)
    print "Hacked message length in bits: {0}".format(hacked_bit_length)

    hacked_message_hex = get_hex(hacked_message)
    print "Hacked message hex version: {0}".format(hacked_message_hex)

    hash_result = sha1(hacked_message)
    print "Hash Result: {0}".format(hash_result)

    # hex_version = get_hex(hash_result)
    # print "Hashed result --> Hex Version: {0}".format(hex_version)