"""
Write a function to find the rectangular intersection of two given love rectangles.

Info is in format:

  my_rectangle = {

    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 5,

    # width and height
    'width': 10,
    'height': 4,

}

"""

def getIntersection(rec1, rec2):
    if rec1['left_x'] + rec1['width'] < rec2['left_x']:
        return None
    if rec2['left_x'] + rec2['width'] < rec1['left_x']: 
        return None
    if rec1['bottom_y'] + rec1['height'] < rec2['bottom_y']:     
        return None
    if rec2['bottom_y'] + rec2['height'] < rec1['bottom_y']:     
        return None
    intersection = {}
    intersection['bottom_y'] = max(rec1['bottom_y'],rec2['bottom_y'])
    intersection['left_x'] = max(rec1['left_x'],rec2['left_x'])
    intersection['width'] = min(rec1['left_x'] + rec1['width']-intersection['left_x'],rec2['left_x'] + rec2['width']-intersection['left_x'])
    intersection['height'] = min(rec1['bottom_y'] + rec1['height']-intersection['bottom_y'],rec2['bottom_y'] + rec2['height']-intersection['bottom_y'])
    return intersection
    
    
my_rectangle = {

    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 5,

    # width and height
    'width': 10,
    'height': 4,

}

my_rectangle2 = {

    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 5,

    # width and height
    'width': 10,
    'height': 4,

}    

print(getIntersection(my_rectangle,my_rectangle2))