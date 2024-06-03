import matplotlib.pyplot as plt

def PlotMesh(vtx,elt,bord = set()):  
    "TP3"
    x = vtx[:, 0]
    y = vtx[:, 1]
    plt.figure(figsize=(8, 6))
    plt.triplot(x, y, elt, 'k-') 
    
    for i in range(len(bord)):
        idx1, idx2 = bord[i]
        X_Point = [x[idx1], x[idx2]]   
        Y_Point = [y[idx1], y[idx2]]  
        plt.plot(X_Point, Y_Point, 'r-')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Maillage')
    plt.grid(True)
    plt.show()