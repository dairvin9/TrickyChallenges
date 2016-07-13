"""

"Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

Write a function that, given a sentence like the one above, along with the position of an opening parenthesis, finds the corresponding closing parenthesis.

Example: if the example string above is input with the number 10 (position of the first parenthesis), the output should be 79 (position of the last parenthesis).

"""

# O(n) time, O(1) space
# I didnt realize untill later that I basically built a stack. Sweet.
def get_match(line, open):
# start with open, 
    close = open + 1
    found = 0 # when fount == 1, we are in buisness
    while close != len(line):
        if line[close] == '(':
            found-=1;
        if line[close] == ')':
            found+=1
            if found == 1:
                return close;
        close+=1
    return None


def testing():
    line = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
    open = 10
    print get_match(line,open)
    
testing()    