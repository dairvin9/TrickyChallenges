"""
You rank players in the game from highest to lowest score. So far you're using an algorithm that sorts in O(n\lg{n})O(nlgn) time, but players are complaining that their rankings aren't updated fast enough. You need a faster sorting algorithm.
"""
"""
    O(n) bucket sort
"""

def sort_scores(scores,highest_possible):
    scores_count = [0] * highest_possible
    #for i in range(highest_possible):
    #    scores_count[i] = 0
    
    for score in scores:
        if score > highest_possible:   
         raise ValueError("Impossible score value!")
        scores_count[score] += 1
    
    sorted = []
    for index,count in enumerate(scores_count):
        for i in range(count):
            sorted.append(index)
    return sorted
    
print sort_scores([3,5,82,3,5,7,1,6,2,89,43],90)    