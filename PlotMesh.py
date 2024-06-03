import matplotlib.pyplot as plt

def PlotMesh(vtx,elt):
    # Extraire les coordonnées x et y des sommets
    x = vtx[:, 0]
    y = vtx[:, 1]

    # Plot du maillage
    plt.figure(figsize=(8, 6))
    plt.triplot(x, y, elt, 'k-')  # voir doc  : k la coleur noire , - droite 
    plt.plot(x, y, 'ro', markersize = 10)  # Affichage des noeuds en rouge
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Maillage')
    plt.grid(True)
    plt.show()