# Your code here
d = {}


def expensive_seq(x, y, z):
    # base case
    if x <= 0:
        t = (x, y, z)
        # create a specific key for t
        d[t] = y + z      
        return d[t]

    if x > 0:    
        # create a tuple holding the values of x, y, and z
        t = (x, y, z)
        # if t is not in the dictionary
        if t not in d:
            # calculate it and add it to d
            d[t] = expensive_seq(x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
            return d[t]
        else:
            return d[t]



if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
