#Write an efficient function that checks whether any permutation of an input string is a palindrome 

# goal: do in log(n) time

    
# My Solution, o(n)
def is_pal(str):
    str = str.lower()
    
    alpha = []
    n = 0
    while n < 26:
        alpha.append(0)
        n = n + 1
    
    for n in str:
        alpha[ord(n) - 97] += 1
         
    odd = 0    
    for n in alpha:
        if n % 2 == 1:
            odd+=1
            if odd > 1:
                return False

    return True 
    
# clever-er solution
def clever(str):
    str = str.lower()
    odd_chars = set()
    for a in str:
        if a in odd_chars:
            odd_chars.remove(a)
        else:
            odd_chars.add(a)

    return len(odd_chars) < 2
    
def testing():
    print clever("civic") == True
    print clever("civil") == False
    print clever("paulpaul") == True
    print clever("pulpul") == True
    print clever("polop") == True
    print clever("look") == False
    
testing()    