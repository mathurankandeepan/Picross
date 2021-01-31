
import config

def parser( nom_fichier ):
    f = open(nom_fichier)

    lines_list = list(f.read().splitlines())

    i=0
    colonnes=[]
    lignes=[]
    while lines_list[i]!='#':
        lignes.append(lines_list[i])
        i=i+1

    colonnes=lines_list[i+1:]

    colonnes = [[int(n) for n in k.split(' ') if n!=''] for k in colonnes]
    lignes = [[int(n) for n in k.split(' ') if n!=''] for k in lignes]

    max_lignes = len(lignes[0])
    for n in lignes:
        if max_lignes < len(n) :
            max_lignes = len(n)

    max_colonnes = len (colonnes[0])
    for n in colonnes:
        if max_colonnes < len(n) :
            max_colonnes = len(n)

    return (len(lignes) , len(colonnes) ,lignes, colonnes, max_lignes, max_colonnes)



def max_len( L ) :
    max = len(L[0])
    for n in L:
        if max < len(n) :
            max = len(n)
    return max