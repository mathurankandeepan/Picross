from tkinter import *
import config
from methode_complete import *
from parser import *

TailleCarre = 0    # Taille de chaque case du tableau sur l'interface graphique
Marge_X = 0         # Marge de l'axe X  pour l'interface graphique
Marge_Y = 0         # Marge de l'axe Y pour l'interĥace graphique

def ecrire_une_ligne( ligne , i , police ):
    """  list [ list [ int ] ] * int * int -> None 
    Ecris dans le canvas la liste de la sequence de la ligne i  """
    ymin =  -police + TailleCarre/8 + i * TailleCarre + Marge_Y 
    xmin =  -police + Marge_X
    for j in ligne[::-1]:
        config.canvas.create_text( xmin , ymin , text= str(j), font=("Helvetica", police ) )
        xmin = xmin - TailleCarre
    return None


def ecrire_lignes ( police ) :
    """  int  -> None
    Ecris dans le canvas la liste des sequences des lignes """
    # l : int 
    l = len( config.Seq_lignes )
    for i in range( l )  :
        ecrire_une_ligne(config.Seq_lignes[i], i + 1 , police )
    return None



def ecrire_une_colonne( colonne , j , police ):
    """  list [ list [ int ] ] * int * int -> None 
    Ecris dans le canvas la liste de la sequence de la colonne j  """
    ymin = -police + TailleCarre/8 + Marge_Y
    xmin = -police + j * TailleCarre  + Marge_X
    for j in colonne[::-1]:
        config.canvas.create_text( xmin , ymin , text= str(j) , font=("Arial", police )  )
        ymin = ymin - TailleCarre
    return None


def ecrire_colonnes ( police ) :
    """ int -> None
    Ecris dans le canvas la liste des sequences des colonnes """
    # l : int 
    l = len( config.Seq_colonnes )

    for i in range( l )  :
        ecrire_une_colonne( config.Seq_colonnes[i], i + 1 , police )
    return None


def ecrire_dimension ( police ) : 
    """ int -> None 
    Ecris dans le canvas les dimensions de la grille"""
    config.canvas.create_text ( Marge_X - 1.5 * TailleCarre, -police + TailleCarre/8 + Marge_Y , text = str(config.N) + " x " + str(config.M) , font = ("Arial", police  ) )
    return None


def init_interface_graphique ( N_init, M_init, lignes, colonnes, max_lignes, max_colonnes, G, str ) :
    """ int * int * list [ list [ int ] ] * list [ list [ int ] ] * int * int * list [ list [ int ] ] -> None
    Initialise l'interface graphique en creant Mafenetre et canvas (valeurs globales) grâce aux différents paramètres """

    global Marge_X
    global Marge_Y
    global TailleCarre

    TailleCarre = int ( min ( 1000 / ( N_init + max_colonnes) , 1000 / ( M_init + max_colonnes ) ) ) # Adapte la taille de la fenetre en fonction de la taille de la grille
    Longueur_Grille = config.M * TailleCarre              # Longueur de la grille axe X
    Hauteur_Grille = config.N * TailleCarre               # Hauteur de la grille axe Y
    Marge_X = TailleCarre* max_lignes                     # Marge de la sequence des colonnes axe X
    Marge_Y = TailleCarre* max_colonnes                   # Marge de la sequence des lignes axe Y
    Longueur_Totale = Longueur_Grille + Marge_X           # Longueur de la fenetre Axe X
    Hauteur_Totale = Hauteur_Grille + Marge_Y             # Hauteur de la fenetre Axe Y

    # Ouverture de la fenetre (Main Window)
    config.Mafenetre = Tk() 
    config.Mafenetre.title( 'Nonogramme ' + str )

    # Ouverture du canvas
    config.canvas = Canvas(config.Mafenetre, width = Longueur_Totale , height = Hauteur_Totale ,bg ='white') # création de la toile
    config.canvas.focus_set()
    config.canvas.pack() 

    # tracer les lignes de la grille
    res = max(config.N + max_lignes, config.M + max_colonnes)
    for i in range( res ) :      
        config.canvas.create_line( i*TailleCarre + Marge_X, 0, i * TailleCarre + Marge_X, Hauteur_Totale , fill='black')
        config.canvas.create_line( 0, i*TailleCarre + Marge_Y , Longueur_Totale,  i*TailleCarre + Marge_Y, fill='black')

    # police : int
    police = int( TailleCarre/2 )

    # ecriture des séquences et de la dimension sur le canvas
    ecrire_lignes( police )
    ecrire_colonnes( police )
    ecrire_dimension( police )

    return None


def refresh_interface_graphique( G ):
    """ Refresh l'interface graphique à partir de la grille G """
    if G == []:
        print( "La grille n'a pas de solution ")
        return None
    # parcours de toute la grille
    for i in range(config.N):
        for j in range(config.M) :
            
            x =  j * TailleCarre + Marge_X
            y =  i * TailleCarre + Marge_Y
            cl = G[i][j]

            # if case vide
            if ( cl == -1 ) : 
                Carre = config.canvas.create_rectangle( x , y, x+TailleCarre, y+TailleCarre,fill='white')
            
            # if case noire
            elif ( cl == 1 ) :
                Carre = config.canvas.create_rectangle( x , y, x+TailleCarre, y+TailleCarre,fill='black')
            
            # if case blanche
            else : 
                config.canvas.create_line( x , y  , x+TailleCarre ,y+TailleCarre,fill='black')
                config.canvas.create_line( x+TailleCarre, y, x,  y+TailleCarre ,fill='black')
    
    return None


def fermeture_interface_graphique():
    """ None -> None 
    Ferme la fenetre graphique """
    config.Mafenetre.mainloop() 
    return None


def affiche_instance_unique_coloration( instance ) :
    """ int -> None 
    Affiche dans une fenetre l'instance apres lui avoir appliqué la méthode coloration"""
    str1 = str(instance)
    N, M, Seq_lignes, Seq_colonnes, max_lignes, max_colonnes = parser("./instances/"+ str1 +".txt")
    G = init_Jeu( N, M, Seq_lignes, Seq_colonnes )
    init_interface_graphique ( N, M, config.Seq_lignes, config.Seq_colonnes, max_lignes, max_colonnes, G, str1)

    (ok, G1) =COLORATION ( G ) 

    refresh_interface_graphique(G1)
    fermeture_interface_graphique()
    return None


def affiche_instance_unique_enumeration( instance ) :
    """ int -> None 
    Affiche dans une fenetre l'instance apres lui avoir appliqué la méthode énumération"""
    str1 = str(instance)
    N, M, Seq_lignes, Seq_colonnes, max_lignes, max_colonnes = parser("./instances/"+ str1 +".txt")
    G = init_Jeu( N, M, Seq_lignes, Seq_colonnes )
    init_interface_graphique ( N, M, config.Seq_lignes, config.Seq_colonnes, max_lignes, max_colonnes, G, str1)
    
    (ok, G1) = ENUMERATION ( G ) 
    
    refresh_interface_graphique(G1)
    fermeture_interface_graphique()
    return None



def affiche_instance_coloration ( debut , fin ) :
    """ int * int -> None 
    Affiche dans une nouvelle fenentre les instances une par une comprises entre debut et fin """
    
    for i in range ( debut , fin + 1):
        affiche_instance_unique_coloration( i )
    
    return None


def affiche_instance_enumeration ( debut , fin ) :
    """ int * int -> None 
    Affiche dans une nouvelle fenentre les instances une par une comprises entre debut et fin """
    
    for i in range ( debut , fin + 1):
        affiche_instance_unique_enumeration ( i )
    
    return None