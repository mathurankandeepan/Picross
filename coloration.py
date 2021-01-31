from methode_incomplete import * 
import copy
import config


def COLORELIG_REC ( G , i , j , l , Nouveau , max , case_noir) :
    """ list [ list [ int ] ] * int * int * int * int * set (int) * int * int -> tuple ( bool , list [ list [ int ] ] , list [int] 
    Colorie par récurrence un max de cases de la ligne i de G """       

    # case de base si toutes les cases parcourues
    if j < 0:
        return ( True , G ,  Nouveau   )
    
    # if somme des cases noirs de la sequence de la ligne i == nombre de cases noires posées 
    if max == case_noir :
        
        # check si la sequence est valide (car elle peut ne pas l'etre)
        if sequence_valide_complet_lignes ( i , config.M - 1 , G ) :
            
            # if true, then colorie en blanc les cases vides de 0 a j
            for k in range ( j + 1 )  :
                if G[i][k] == -1 :
                    change_couleur( i , k , 0 , G ) 
                    Nouveau.add ( k )      
            return ( True , G ,  Nouveau)
        
        # else la sequence est fausse
        return (False, [], set () )

    # if case noir
    if  G[i][j] == 1  :
        case_noir += 1

    # else case vide
    elif G[i][j] == -1 : 

        # noir : bool   
        noir = False                               # initialisation
        # blanc : bool 
        blanc = False                              # initialisation

        # blanc = True if apres avoir colorie en blanc la case ( i , j ), la sequence de la ligne i est valide else return False
        change_couleur( i , j , 0 , G )
        blanc = sequence_valide_complet_lignes( i , j , G ) 
        # noir = True if apres avoir colorie en noir la case ( i , j ), la sequence de la ligne i est valide else return False
        change_couleur(i, j, 1, G)
        noir = sequence_valide_complet_lignes( i , j , G ) 

        # if ne peut pas colorier en blanc et en noir, then return False    
        if (not blanc) and (not noir) :
            return (False , G , set () )


        # if on peut colorier en noir mais pas en blanc then colorie la case en noir et return COLORELIG_REC de la case suivante avec un TTL
        elif (noir and not blanc) :      
            Nouveau.add( j )
            case_noir +=1

        # if on peut colorier en blanc mais pas en noir then colorie la case en blanc, ajoute la colonne  à ColoneAVoir et return COLORLIG de la case suivante
        elif (blanc and not noir) :
            change_couleur(i,j,0,G)
            Nouveau.add(j)

        # else on ne peut pas savoir entre noir et blanc donc return COLORELIG_REC de la case suivante 
        else :
            change_couleur(i,j,-1,G)

    return COLORELIG_REC ( G , i , j - 1  , l , Nouveau , max , case_noir)


def COLORELIG ( G , i ) :
    """ list [ list [ int ] ] * int -> tuple ( bool , list [ list [ int ] ] , set (int) )
    Appelle la fonction COLORELIG_REC qui colorie par récurrence un max de cases de la ligne i de G"""
    # l : int  
    l = len ( config.Seq_lignes [i])
    # Nouveau : set
    Nouveau = set()
    # max : int
    max = 0
    # case_noir : int 
    case_noir = 0
    for k in range ( l ) :
        max += config.Seq_lignes[i][k]
        
    return COLORELIG_REC ( G , i , config.M - 1 , l , Nouveau, max , case_noir)


def COLORECOL_REC ( G , i , j , l ,  Nouveau  , max , case_noir) : 
    """ list [ list [ int ] ] * int * int * int * int * set (int) * int * int  -> tuple ( bool , list [ list [ int ] ] , list [int] 
    Colorie par récurrence un max de cases de la colonne j de G """

    # case de base si toutes les cases parcourues
    if i < 0:
        return ( True , G ,  Nouveau )
    
    
   # if somme des cases noirs de la sequence de la ligne i == nombre de cases noires posées 
    elif max == case_noir :
        # check si la sequence est valide (car elle peut ne pas l'etre)
        if sequence_valide_complet_colonnes ( config.N - 1 , j , G ) :
            
            # if true, then colorie en blanc les cases vides de 0 a j
            for k in range ( i + 1 )  :
                if G[k][j] == -1 :
                    change_couleur( k , j , 0 , G ) 
                    Nouveau.add ( k )  
            return ( True , G ,  Nouveau)
        
        # else retourne False car la sequence n'est valide
        return (False, [], set ())

    # if case noire    
    if  G[i][j] == 1 :
        case_noir +=1

    # else case vide
    elif G[i][j] == -1 :    
    
        # noir : bool   
        noir = False
        # blanc : bool   
        blanc = False  

        # blanc = True if apres avoir colorie en blanc la case ( i , j ), la sequence de la colonne j est valide else return False
        change_couleur( i , j , 0 , G )
        blanc = sequence_valide_complet_colonnes( i , j , G )
        # noir = True if apres avoir colorie en noir la case ( i , j ), la sequence de la colonne j est valide else return False
        change_couleur( i , j , 1 , G )
        noir = sequence_valide_complet_colonnes ( i , j , G )     

        # if ne peut pas colorier en blanc et en noir, then return False    
        if (not blanc) and (not noir) :
            return (False , G , set () )

        # if on peut colorier en noir mais pas en blanc then colorie la case en noir et return COLORECOL_REC de la case suivante avec un TTL
        elif (noir and not blanc) :      
            Nouveau.add( i )
            case_noir +=1

    
        # if on peut colorier en blanc mais pas en noir then colorie la case en blanc, ajoute la colonne  à LignesAVoir et return COLORECOL_REC de la case suivante
        elif (blanc and not noir) :
            change_couleur( i , j , 0 , G )
            Nouveau.add( i )

        # else on ne peut pas savoir entre noir et blanc donc return COLORECOL_REC de la case suivante 
        else :
            change_couleur( i , j  , -1 , G )
   
    return COLORECOL_REC ( G , i - 1 , j , l , Nouveau , max , case_noir )



def COLORECOL ( G , j ) :
    """ list [ list [ int ] ] * int -> tuple ( bool , list [ list [ int ] ] , set (int) )
    Appelle la fonction COLORECOL_REC qui colorie par récurrence un max de cases de la colonne j de G"""
    # l : int  
    l = len ( config.Seq_colonnes [j])   
    # Nouveau : set
    Nouveau = set() 
    # max : int
    max = 0
    # case_noir : int 
    case_noir = 0
    for k in range ( l ) :
        max += config.Seq_colonnes[j][k]
    return COLORECOL_REC ( G , config.N - 1  , j , l , Nouveau , max , case_noir )







def COLORATION ( G ) :
    """ list [ list [ int ] ] -> tuple ( bool , list [ list [ int ] ] ) 
    Algortihme de resolution partielle qui retourne quand c'est possible,
    la grille resolue"""

    # G_copy : list[ list [ int ] ] 
    G_copy = copy.deepcopy( G )                  # copie de la grille G pour ne pas la modifer
    # LignesAVoir : set ( int )                
    LignesAVoir = set ()
    # ColonnesAvoir : set ( int )
    ColonnesAVoir = set ()
    
    # Initialisation 
    for i in range(config.N) :
        # LignesAVoir prend les valeurs de 0 à N - 1
        LignesAVoir.add(i)
    for j in range(config.M) :
        # ColonnesAvoir prend les valeurs de 0 à M - 1
        ColonnesAVoir.add(j)

    # Tant qu'il y a des lignes ou des colonnes a voir  
    while ( ( len( LignesAVoir ) != 0 ) or ( len ( ColonnesAVoir ) != 0) ) :
        
        for i in  LignesAVoir   :

            # colorie par recurrence un max de cases de la ligne i de G_copy
            ok , G_copy , L = COLORELIG ( G_copy , i )

            # if ok == False then retourne Faux car detection d'impossibilite
            if  ok == False :
                return (False,[])
            
            # else concatenation de ColonnesAvoir et des colonnes des nouvelles cases coloriees
            ColonnesAVoir = ColonnesAVoir | L
        
        # Reset l'ensemble des lignes qui viennent d'etre parcouru
        LignesAVoir = set()
        
        for j in  ColonnesAVoir :
            # colorie par recurrence un max de cases de la colonne j de G_copy
            ok , G_copy , L = COLORECOL ( G_copy , j )                 

            # if ok == False then retourne Faux car detection d'impossibilite
            if ok == False :
                return (False,[])
            
            # else concatenation de ColonnesAvoir et des colonnes des nouvelles cases coloriees
            LignesAVoir = LignesAVoir | L
            
        # Reset l'ensemble des colonnes qui viennent d'etre parcouru
        ColonnesAVoir = set()

    # if toutes les cases de G_copy sont coloriees retourne True 
    for i in range(config.N) :
        for j in range(config.M) :
            # if case non colorié then retourne None
            if G_copy[i][j] == -1 :
                return (None,G_copy)

    return (True,G_copy)   