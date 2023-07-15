
def to_str(num, base):
    digits = "01234556789ABCDEF"

    if num < base:
        return digits[num]
    else:
        return to_str(num // base, base) + digits[num % base]

