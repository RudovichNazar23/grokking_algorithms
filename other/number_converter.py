from stack import Stack


def binary_number(num):
    remstack = Stack()

    while num > 0:
        rem = num % 2
        remstack.push(rem)
        num //= 2

    binstring = ""

    while not remstack.is_empty():
        binstring += str(remstack.pop())
    return binstring


def number_converter(num, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while num > 0:
        rem = num % base
        remstack.push(rem)
        num //= base

    conv_number = ""

    while not remstack.is_empty():
        conv_number += str(digits[remstack.pop()])
    return conv_number


print(number_converter(5, 8))
