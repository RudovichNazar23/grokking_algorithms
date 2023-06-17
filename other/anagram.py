
def anagram(s1, s2):
    al1 = [i.lower() for i in s1]
    al2 = [i.lower() for i in s2]

    al1.sort()
    al2.sort()

    x = 0
    matches = True

    while x < len(s1) and matches:
        if al1[x] == al2[x]:
            x += 1
        else:
            matches = False
    return matches

