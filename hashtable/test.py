def djb2(key):
    """
    DJB2 hash, 32-bit

    Implement this, and/or FNV-1.
    """
    hash = 5381
    key = str(key)
    for x in key:
        hash = (( hash << 5) + hash) + ord(x)
    return hash

capacity = 8

print(djb2(10))
print(djb2('princess'))
print(djb2('princess')%capacity)