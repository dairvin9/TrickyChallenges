# Write a recursive function for generating all permutations of an input string. Return them as a set.

def permutate(string):
    if len(string) == 0:
        return {}
    if len(string) == 1:
        print string
        return { string }
    if len(string) > 1:
        current = permutate(string[1:])
        for c in current.copy():
            index = 0
            while len(c) >= index:
                new_string = c[:index] + string[0] + c[index:]
                current.add(new_string)
                index += 1
            current.remove(c)    
        return current    
#    if 
print permutate('cat')
print permutate('cats')
print permutate('sas')
print permutate('')
print permutate('Denise')
# Long words work, but take forever #recursion
# print permutate('Maddie-pie')
# print permutate('Esperanza')