from jeu import *
from interface_graphique import *
from temps import *

def menu ():

    while (True):
        print (""" Bienvenue! Veuillez choisir une option:
                    ## Affichage Graphique ##
                        1. Affiche une instance avec coloration
                        2. Affiche plusieurs instances avec coloration
                        3. Affiche une instance avec enumeration
                        4. Affiche plusieurs instances enumeration

                    ## Temps d'execution ##
                        5. Affiche le temps moyen pour une instance avec coloration
                        6. Affiche le temps moyen global avec coloration
                        7. Affiche le temps moyen pour une instance enumeration
                        8. Affiche le temps moyen global avec enumeration
                    
                        0. exit """)

        choix = input( "Selectionez votre choix : ")
        if choix == "1":
            instance = input( "Veuillez introduire le numero de l'instance a afficher : ") 
            affiche_instance_unique_coloration( instance ) 

        elif choix == "2":
            debut = int(input( "Veuillez introduire le numero de la premiere instance a afficher : ") )
            fin = int (input( "Veuillez introduire le numero de la derniere instance a afficher : ") )

            affiche_instance_coloration( debut , fin ) 

        elif choix == "3":
            instance = input( "Veuillez introduire le numero de l'instance a afficher : ") 
            affiche_instance_unique_enumeration( instance ) 

        elif choix == "4":
            debut = int(input( "Veuillez introduire le numero de la premiere instance a afficher : ") )
            fin = int (input( "Veuillez introduire le numero de la derniere instance a afficher : ") )

            affiche_instance_enumeration( debut , fin ) 

        elif choix == "5":
            instance = input( "Veuillez introduire le numero de l'instance : ") 
            nb = int (input( "Veuillez introduire le numero de tests a effectuer : ") )
            temps_moyen_coloration ( instance , nb )
        
        elif choix == "6":
           debut = int(input( "Veuillez introduire le numero de la premiere instance : ") )
           fin = int (input( "Veuillez introduire le numero de la derniere instance : ") )
           nb =int ( input( "Veuillez introduire le numero de tests a effectuer : ") )
           temps_moyen_global_coloration ( debut, fin, nb )

        elif choix == "7":
           instance = input( "Veuillez introduire le numero de l'instance : ") 
           nb = int( input( "Veuillez introduire le numero de tests a effectuer : ") )
           temps_moyen_enumeration ( instance , nb )

        elif choix == "8":
           debut = int(input( "Veuillez introduire le numero de la premiere instance : ") )
           fin = int (input( "Veuillez introduire le numero de la derniere instance : ") )
           nb = int (input( "Veuillez introduire le numero de tests a effectuer : ") )
           temps_moyen_global_enumeration ( debut, fin, nb )  
        
        elif choix == "0":
            break
        else :
            print ("invalid input")

        ok = input ( "Faire un autre choix? y/n ")
        if (ok =="n"):
            print ("Au revoir!")
            break

    return None
        
menu()