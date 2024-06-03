import numpy as np

def Boundary(elt):
    boundary_edges = set()
    for c in range(len(elt)):
        K_c_triangle = elt[c,:]
        for j in range(3):
            Face = (K_c_triangle[j % 3], K_c_triangle[(j+1) % 3])
            Face = tuple((sorted(Face)))
            if Face in boundary_edges:
                boundary_edges.remove(Face) 
            else:
                boundary_edges.add(Face)
    return np.array(list(boundary_edges))