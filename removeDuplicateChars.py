# remove duplicate characters in string without additional buffer

s1 = 'denise'
s2 = 'sassafrass'
s3 = 'sass'

# assumptions: ascii v unicode (lets assume ascii)
# uppercase and lowercase are different

# Brutest of force:
# could walk through the string and remove all extra characters
# If i could have extra space, make a set and then as i find something not in it i would replace it
# If I dont need to keep the order of the string, i could sort


def removeDuplicates(s):
    if type(s) != str:
        raise TypeError('Function removeDuplicates requires input of type str, found ' + str(type(s)))
    if len(s) < 2:
        return s
    

    ascii = [False]*256
    length = len(s)
    index = 0
    while index < length:
        char = s[index]
        
        if ascii[ord(char)] == True:
            s = s[:index] + s[index + 1 :] 
            length -=1
        else:
            ascii[ord(char)] = True
            index += 1    
    return s        
            
# testing
cases = [s1, s2, s3, "a", "", 4]
for case in cases:
    try:
        print(removeDuplicates(case))
    except Exception as e:
        print(str(e))