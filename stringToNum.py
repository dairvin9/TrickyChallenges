from __future__ import division

# Convert String to Num
conversion_constant = 48

# What about decimals
def StringToNum(string):
    if not isinstance(string,basestring):
        raise ValueError("You must enter a string")
    total = 0
    
    index_of_decimal = len(string)
    decimal_found = False
    
    index = 0
    factor = len(string) - 1 
    if '.' in string:
        factor -= 1
    while index < len(string):    
        if index == 0 and string[index] == '-':
            index+=1
            continue
        if string[index] == '.':
            if decimal_found:
                raise ValueError("A number can only have one decimal point")
            index_of_decimal = index
            index += 1
            decimal_found = True
            continue
        if (ord(string[index])-conversion_constant) < 0 or (ord(string[index])-conversion_constant) > 9:
            raise ValueError("All characters must be numeric or '-' or '.'")
        else:
            total+= (ord(string[index])-conversion_constant)*(10**factor)
            factor-=1
        index += 1

    if decimal_found:
        total = total / (10**(len(string) - index_of_decimal - 1))    
        
    if string[0]  == '-':
        total*=-1
    return total    

print StringToNum("2.5")
print StringToNum("91.3256765")    
print StringToNum("91324253675876543256765")    
print StringToNum("43")        
print StringToNum("-23443")        
print StringToNum("0")        
print StringToNum("0.0")        
print StringToNum("0.0254678")        

try:
    print StringToNum(None)
except(ValueError):
    print "Whew this failed."
try:
    print StringToNum("Taco")
except(ValueError):
    print "Whew this failed."   
try:
    print StringToNum("1.2.3.5")
except(ValueError):
    print "Whew this failed."      