# To prove this, let's write a function to tell us if a full deck of cards shuffled_deck is a single riffle of two other halves half1 and half2.
def isRiffle(h1, h2, shuffled):
    half1_index = 0
    half2_index = 0
    for x in shuffled:
        try:
            if x == h1[half1_index]:
                half1_index+=1
                continue
        except IndexError:
            pass
        try:
            if x == h2[half2_index]:
                half2_index+=1
                continue
        except IndexError:
            pass
        return False

    return True

half1 = [1,2,3,4,5]
half2 = [6,7,8,9,10]
shuffled = [1,2,3,4,5,6,7,8,9,10]

print(isRiffle(half1,half2,shuffled))

half1 = [1,2,3,4,5]
half2 = [6,7,8,9,10]
shuffled = [1,6,2,7,3,8,4,9,5,10]

print(isRiffle(half1,half2,shuffled))

half1 = [1,2,3,4,5]
half2 = [6,7,8,9,10]
shuffled = [1,2,7,6,3,8,4,9,5,10]

print(isRiffle(half1,half2,shuffled))

print(isRiffle([],[1],[1]))