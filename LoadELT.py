import numpy as np

def LoadELT(filename): 
    elements = []

    is_reading_elemnts = False
    
    file = open(filename,'r')
    
    lines = file.readlines()
    
    for l in lines:
        if l.startswith("$Elements"):
            is_reading_elemnts = True
            continue
    
        elif l.endswith("FinElements"):
            is_reading_elemnts = False
    
        elif is_reading_elemnts:
            triangles = l.split()
    
            if len(triangles) >= 4:
                elements.append([int(triangles[1]), int(triangles[2]),int(triangles[3])])
    
    file.close()
    return np.array(elements)