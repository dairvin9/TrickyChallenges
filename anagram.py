def anagram(s1, s2):
    letters = {}
    for letter in s1:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter]+=1
    for letter in s2:
        if letter not in letters:
            return False
        if letters[letter] == 1:
            letters.pop(letter)
        else:
            letters[letter]-=1
    return letters == {}        
            
            
print(anagram("yes","sey"))
print(anagram("Denise","esineD"))

print(anagram("see","sey"))