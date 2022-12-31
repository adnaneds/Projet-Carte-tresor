# -*- coding: utf-8 -*-


import numpy as np
from collections import defaultdict
from Carte import Carte
from Aventurier import Aventurier
from Tresor import Tresor

def creer_carte(nb_case_hauteur, nb_case_longueur):    
    """
    creation d'une carte vide
    """
    carte = np.empty((nb_case_hauteur, nb_case_longueur), dtype=object)
    #for axe_0 in range(nb_case_largeur):
    #    for axe_1 in range(nb_case_longueur):
    #        carte[axe_0, axe_1] = "."
            
    print(f"Creation d'une carte vide de dimension ({nb_case_longueur},{nb_case_hauteur})")
    return carte


def insert_in_carte(carte, pos_hor, pos_vert, valeur):
    """
    la carte est une matrice, les pos_hor, pos_vert sont des entiers, valeur est un objet 
    """
    carte[pos_vert, pos_hor] = valeur
    print(f"{valeur} est insersé dans la carte, dans la position ({pos_hor},{pos_vert})")



def convert_to_dict(path_fichier_input):

    dictio_stock = defaultdict(list)
    
    with open(path_fichier_input) as f:
        lines = f.readlines()
        #print(lines)
        #print(type(lines[0]))
        #print(type(lines))
        
        for line in lines:
            line = line.replace("\n","")  # cleaning
            line.split('-')
            key = line.split('-')[0]
            value = line.split('-')[1::]
            dictio_stock[key].append(value)    
    
    return dictio_stock

##############


################################ Etape 1 ##########################

#### Parcourir le dictionnaire et extraire toutes les infos.


###############################################################################

############ Representation carte 



def initialiser_carte(path_file):
    """
    fonction qui remplit la carte du depart. 
    
    """
    
    dictio_stock = convert_to_dict(path_file)     #le dictionnaire pour stocker les données
    print(" Le dictionnaire pour stocker les données \n ")
    print(dictio_stock)  # sorted, like the input
    print('\n')
    
    dictio_stock_to_classes = defaultdict(list)
    
    for key, val in dictio_stock.items():
        
        ### Carte
        if key=='C ':
            axe_hor_c = int(val[0][0]) 
            axe_vert_c = int(val[0][1])
            
            print(f"Nous avons une carte de dimension {axe_hor_c},{axe_vert_c} \n")   
            la_carte = creer_carte(axe_vert_c, axe_hor_c)
        
            ### les Montagnes
        if key=='M ':
            
            nb_montagne = len(val)
            print(f"Nous avons {nb_montagne} montagne(s) sur la carte")
            
            for mont in val:
                
                axe_hor_m  = int(mont[0])
                axe_vert_m  = int(mont[1])
                print(f" - une montagne en position ({axe_hor_m},{axe_vert_m}) \n")
                insert_in_carte(la_carte, axe_hor_m, axe_vert_m, key) 

                dictio_stock_to_classes['M'].append([axe_hor_m, axe_vert_m])
                print(" insertion des montagnes dans le dict_classes")    
        
        if key=='T ':
                
            nb_case_tresor = len(val)
            print(f"Nous avons {nb_case_tresor} case(s) contenant un ou plusieurs tresor(s) sur la carte")
        
            for tres in val:
                if len(tres)==2:
                    axe_hor_t  = int(tres[0])
                    axe_vert_t = int(tres[1])
                    
                    print(f"- On a un tresor à la position ({axe_hor_t},{axe_vert_t})")    
                    insert_in_carte(la_carte, axe_vert_t, axe_hor_t, key) 
                    dictio_stock_to_classes['T'].append([axe_vert_t, axe_hor_t, 1])
                    
                if len(tres)==3:
                    nb_tresor_case = int(tres[2])
                    axe_hor_tt = int(tres[0])
                    axe_vert_tt = int(tres[1])
                    print(f"- On a {nb_tresor_case} tresors à la position ({axe_hor_tt},{axe_vert_tt}) \n") 
                    insert_in_carte(la_carte, axe_hor_tt, axe_vert_tt, key+'('+str(nb_tresor_case)+')') 
                    
                    dictio_stock_to_classes['T'].append([axe_hor_tt, axe_vert_tt, nb_tresor_case])
                    
           #dictio_stock_to_classes['T'] = Tresor(dictio_stock_to_classes['T'])
                
        
        ### les Aventuriers
        if key=='A ':
            
            nb_aventurier = len(val)    
            print(f"Nous avons {nb_aventurier} aventurie(s)")
            
            for avent in val:
                
                nom_a = avent[0]
                axe_hor_a = int(avent[1])
                axe_vert_a  = int(avent[2])
                orientation_a = avent[3]
                chemin_a = avent[4]
                chemin_a_ = chemin_a.replace(" ", "")
                chemin_to_list = [letter for letter in chemin_a_] 
                
                print(f" - l'aventurier(e) {nom_a} est en position ({axe_hor_a},{axe_vert_a}), d'orientation {orientation_a} suivra le chemin {chemin_a} \n")
                insert_in_carte(la_carte, axe_hor_a, axe_vert_a, nom_a) 

                dictio_stock_to_classes['A'].append(Aventurier(nom_a, axe_hor_a, axe_vert_a, orientation_a, chemin_to_list, dictio_stock_to_classes['T'], dictio_stock_to_classes['M']))
                print(" insertion d'aventurier dans le dict_classes")
                
                

    print("\n")
    #print("Le dictionnaire pour stocker les données pour les classes \n ")
    #print(dictio_stock_to_classes)
    #print('\n')
    carte_0 = la_carte
    
    return carte_0, dictio_stock_to_classes







#############################################           Main               ##############################################

if __name__ == "__main__":




####################################################################################################
############################ Test lecture et sortie de la carte ###############
    
    print("Test lecture et sortie de la carte")

    
    path = r'C:\Users\adnan\Desktop\M2 Adnane\insertion prof et cv\Computer vision Test\entretien_technique_Cali\entretien_technique_Cali\input.txt'
    la_carte, dictio_to_classe = initialiser_carte(path)
    
    print(" Etape 1 achevée")
    print("La carte de depart est la suivante : ", "\n")
    print(la_carte)
    print("\n")
    
    print("le dictionnaire contenant les données pour les classes est sous le format suivant :", "\n")
    #
    print(dictio_to_classe)
    print("\n")

#####################################################################################################
#####################################################################################################
            
            
            
#######################################################################################################
############################## Etape 2: Simulation des mouvements muni des classes



###############################################################################
######## Simulation des mouvements :


    ma_carte = Carte(la_carte)
    dictio_to_classe
    #tresor =  dictio_to_classe['T']
    
    #aventurier = Aventurier('Lara', 1, 1, ' S ', ['A','A','D','A','D','A','G','G'])

    #chemin_for_while
    aventurier_1 = dictio_to_classe['A'][0]
    print(aventurier_1.actual_pos())
    
    aventurier_1
    test_coordonnée_tresor = aventurier_1.coordonne_tresor
    print('coord tresor')
    print(test_coordonnée_tresor)
    print("\n")
    test_coordonnée_montagne = aventurier_1.coordonne_montagne
    print('coord montagnes')
    print(test_coordonnée_montagne)
    
    for aventurier_ in dictio_to_classe['A']:
        task = aventurier_ 
    #while len(aventurier.chemin_for_while)==0:
        #do 
        
    print("chemin aventurier")
    print(aventurier_1.chemin)
    print("\n")
       
    print("Debut de la chasse")    
    aventurier_1.chasser()
    print("Fin de la chasse")
    print("\n")
    
    position_final = aventurier_1.actual_pos()
    print(f"L'aventurier(e) a collecté(e) {aventurier_1.Nb_tresor_col} trésor et fini en position {position_final}")
    print("\n")