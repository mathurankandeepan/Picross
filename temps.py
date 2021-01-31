import time 
from methode_complete import * 
from parser import *



def temps_moyen_coloration ( instance , nombre_de_tests ):
    """ int * int -> None
    Affiche le temps en seconde que prend la fonction COLORATION sur l'instance en effectuant une moeyenne de nombre_de_tests"""
    # res : int
    res = 0
    
    for i in range ( nombre_de_tests ) : 
        str1 = str( instance )
        # Initialisation du chronometre
        time_start = time.time()

        N, M, Seq_lignes, Seq_colonnes, max_lignes, max_colonnes = parser("./instances/"+ str1 +".txt")
        G = init_Jeu( N, M, Seq_lignes, Seq_colonnes )
        (ok, G1) =COLORATION ( G ) 

        # Fin du chronometre
        time_end = time.time()
        res += time_end - time_start

    print ("Instance ", str1 , " \tResolution : " , ok  , "\ttemps : ", round ( res/nombre_de_tests , 6 )  , " secondes" )
    return None


def temps_moyen_global_coloration ( instance_debut, instance_fin, nombre_de_tests ) : 
    """ int * int * int -> None
    Affiche le temps en seconde que prend la fonction COLORATION sur les instances dans [instance_debut:instance_fin] en effectuant une moyenne de nombre_de_tests"""
    
    # time_start_global : float
    time_start_global = time.time()

    for i in range ( instance_debut , instance_fin + 1 ) :
        # calcule du temps global       
        temps_moyen_coloration ( i , nombre_de_tests )

    # time_end_global : float
    time_end_global = time.time()
    print ( "temps global = ", (time_end_global - time_start_global)/nombre_de_tests  )
    return None



def temps_moyen_enumeration ( instance , nombre_de_tests ):
    """ int * int -> None
    Affiche le temps en seconde que prend la fonction ENUMERATION sur l'instance en effectuant une moeyenne de nombre_de_tests"""
    # res : int 
    res = 0
    
    for i in range ( nombre_de_tests ) : 
        str1 = str( instance )
        # Initialisation du chronometre
        time_start = time.time()

        N, M, Seq_lignes, Seq_colonnes, max_lignes, max_colonnes = parser("./instances/"+ str1 +".txt")
        G = init_Jeu( N, M, Seq_lignes, Seq_colonnes )
        (ok, G1) = ENUMERATION ( G )

        # Fin du chronometre
        time_end = time.time()
        res += time_end - time_start

    print ("Instance ", str1 , " \tResolution : " , ok  , "\ttemps : ", round ( res/nombre_de_tests , 6 )  , " secondes" )
    return None

def temps_moyen_global_enumeration ( instance_debut, instance_fin, nombre_de_tests ) : 
    """ int * int * int -> None
    Affiche le temps en seconde que prend la fonction ENUMERATION sur les instances dans [instance_debut:instance_fin] en effectuant une moyenne de nombre_de_tests"""
    
    # time_start_global : float
    time_start_global = time.time()

    for i in range ( instance_debut , instance_fin + 1 ) :
        # calcule du temps global
        temps_moyen_enumeration ( i , nombre_de_tests )

    # time_end_global : float
    time_end_global = time.time()

    print ( "temps global = ", (time_end_global - time_start_global)/nombre_de_tests )
    return None