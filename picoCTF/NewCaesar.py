import string

c = 'dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac'

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

for j in range(16):
    a = ''
    for i in c:
        a += ALPHABET[(ord(i)-LOWERCASE_OFFSET+j) % len(ALPHABET)]
    # print(a)
    for i in range(0,len(a),2):
        binary="{:04b}{:04b}".format((ord(a[i])-LOWERCASE_OFFSET),(ord(a[i+1])-LOWERCASE_OFFSET))
        print(chr(int(binary,2)),end='')
    print()
