import numpy as np


def LoadVTX(filename):
    nodes = []  
    is_reading_nodes = False  

    file = open(filename, 'r')
    lines = file.readlines()
    
    for line in lines:
        if line.startswith("$Noeuds"):
            is_reading_nodes = True 
            continue
        elif line.startswith("$FinNoeuds"):
            is_reading_nodes = False 
            continue
        elif is_reading_nodes:
            cords = line.split()
            if len(cords) >= 3:
                nodes.append([float(cords[1]), float(cords[2])])
                
                     
    file.close()
    return np.array(nodes)
