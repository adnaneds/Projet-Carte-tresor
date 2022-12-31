# -*- coding: utf-8 -*-


import numpy as np
from collections import defaultdict




def creer_carte(nb_case_largeur, nb_case_longueur):    
    """
    creation d'une carte vide
    """
    carte = np.empty((nb_case_largeur, nb_case_longueur), dtype=object)
    print(f"Creation d'une carte vide de dimension ({nb_case_largeur},{nb_case_longueur})")
    return carte


def insert_in_carte(carte, pos_hor, pos_vert, valeur):
    """
    la carte est une matrice, les pos_hor, pos_vert sont des entiers, valeur est un objet 
    """
    carte[pos_hor, pos_vert] = valeur
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
    
    dictio_stock = convert_to_dict(path_file)
    print("le dictionnaire pour stocker les données")
    print(dictio_stock)  # sorted, like the input
    print('\n')
    
    for key, val in dictio_stock.items():
        
        ### Carte
        if key=='C ':
            axe_hor_c = int(val[0][0]) 
            axe_vert_c = int(val[0][1])
            
            print(f"Nous avons une carte de dimension {axe_hor_c},{axe_vert_c} \n")   
            la_carte = creer_carte(axe_hor_c, axe_vert_c)
            
        
        ### les Aventuriers
        if key=='A ':
            
            nb_aventurier = len(val)    
            print(f"Nous avons {nb_aventurier} aventurie(s)")
            
            for avent in val:
                
                nom_a = avent[0]
                axe_hor_a = int(avent[1])
                axe_vert_a = int(avent[2])
                orientation_a = avent[3]
                chemin_a = avent[4]
                
                print(f" - l'aventurier(e) {nom_a} est en position ({axe_hor_a},{axe_vert_a}), d'orientation {orientation_a} suivra le chemin {chemin_a} \n")
                insert_in_carte(la_carte, axe_hor_a, axe_vert_a, nom_a) 
        
        ### les Montagnes
        if key=='M ':
            
            nb_montagne = len(val)
            print(f"Nous avons {nb_montagne} montagne(s) sur la carte")
            
            for mont in val:
                
                axe_hor_m = int(mont[0])
                axe_vert_m = int(mont[1])
                print(f" - une montagne en position ({axe_hor_m},{axe_vert_m}) \n")
                insert_in_carte(la_carte, axe_hor_m, axe_vert_m, key) 


        ### les tresors
        if key=='T ':
            
            nb_case_tresor = len(val)
            print(f"Nous avons {nb_case_tresor} case(s) contenant un ou plusieurs tresor(s) sur la carte")
        
            for tres in val:
                if len(tres)==2:
                    axe_hor_t = int(tres[0])
                    axe_vert_t = int(tres[1])
                    
                    print(f"- On a un tresor à la position ({axe_hor_t},{axe_vert_t})")    
                    insert_in_carte(la_carte, axe_hor_t, axe_vert_t, key) 
                    
                if len(tres)==3:
                    nb_tresor_case = int(tres[2])
                    
                    axe_hor_tt = int(tres[0])
                    axe_vert_tt = int(tres[1])
                    print(f"- On a {nb_tresor_case} tresors à la position ({axe_hor_tt},{axe_vert_tt}) \n") 
                    insert_in_carte(la_carte, axe_hor_tt, axe_vert_tt, key+'('+str(nb_tresor_case)+')') 
                    

    print('\n')
    carte_0 = la_carte
    print("la carte de départ \n")
    return carte_0


###################################################################################################
######################## Test lecture et sortie de la carte ###############

path = r'C:\Users\adnan\Desktop\M2 Adnane\insertion prof et cv\Computer vision Test\entretien_technique_Cali\entretien_technique_Cali\input.txt'
la_carte = initialiser_carte(path)
print(la_carte)


#####################################################################################################
#####################################################################################################
         
         
         
         
         
         
#########################################################
##################### Etape 2: Simulation des mouvements 


#### Idées et definition des variables importantes
## voir l'ordre, des variables, par exemple l'ordre des tresors n'est important, mais les aventuriers oui

### variables lié au terrain

## Montagne
# chaque montagne à une position, lorsque l'aventurier se met face à la montagne, skip to next mouvement
# definir les montagnes en tant qu'obstacles , acev leurs coordonnées



## Tresor
NB_Tresor = 0

# Add to class, chaque tresor a une position et un nombre 
# decremebter au cas de prise
## condition de prise du tresor, si ça coincide avec les coordonnées

## Tresor comme dictionnaire aussi, voir l'ordre,
# si tresor, 


## Variables liées aux aventuriers
# initial
# chaque aventurier a une position

####### Tout ces mouvement vont impacter la carte, au sens des coordonnées qui vont changer, et aussi la situation de la carte

def orientation(var):
    
    if var== ' S ':
        pass    
    if var== ' O ':
        pass
    if var== ' E ':
        pass
    if var== ' N ':    
        pass
    
def move(direction):
    
    return direction



def avancer(var):
    
    return "tout droit, selon la direction"


def tourner_gauche(var):
    
    return "gauche"


def tourner_groite(var):
    
    return "droite"


def prendre(var):
    
    return "retirer un tresor, s'il existe"

def skip(var):
    return "passer au mouvement suivant"





#for mov in mouvements:
    #'mov'+'pos' == 'obstacle':
    #do 'skip'







###############################################################################
######## Simulation des mouvements :
    


class Carte:
    
    def __init__(self, file):
        
        #self.file = file
        """
        # variables de class
        dictio_stock = {}
        
        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                line = line.replace("\n","")  # cleaning
                line.split('-')
                key = line.split('-')[0]
                value = line.split('-')[1::]
                dictio_stock[key] = value
        """
        pass
        # la carte est sous forme d'un tableau

        #coordonnées_carte =  
        #coordoonées_aventurier = 
        #coordonnées_tresor = 
        #coordonnées_montagne = 
    
    def position(self, objet):
        
        if objet== 'A ': 
            pass 
        if objet== 'M ':
            pass
    
    def boussole(self):
        pass
        
    def read(self):
        pass
    
    def construire_carte(self):
        """
        Initialiser la carte
        """
        pass                    


class Aventurier(Carte) :
    

    def __init__(self, nom, axe_hor, axe_vert, orient, chemin, carte):
        self.nom = nom
        self.orient = orient
        self.axe_hor = axe_hor
        self.axe_vert = axe_vert
        self.chemin = chemin
        
        #
        self.pas_x = 0
        self.pas_y = 0
    
    def orientation(self):
        
        if self.orient == ' N ':
            self.pas_x = 0
            self.pas_y = -1
        
        if self.orient == ' O ':
            self.pas_x = -1
            self.pas_y = 0
            
        if self.orient == ' S ':
            self.pas_x = 0
            self.pas_y = 1
            
        if self.orient == ' E ':
            self.pas_x = 1
            self.pas_y = 0
        
        print("orientation")    
        ### idées, ou :  , vers :    ; 
        #  ou je vois:  N, vers ou je vais: D-> E (+1), G-> O(-1)  ;
        #  ou je vois:  S, vers ou je vais: D-> O (-1), G-> E(+1)  ;
        #  ou je vois:  E, vers ou je vais: D-> S (+1), G-> N(-1)  ;
        #  ou je vois:  O, vers ou je vais: D-> N (-1), G-> S(+1)  ;

    
    def tourner_gauche(self):

        orient_preced = self.orient
        
        if orient_preced == ' N ':
            self.pas_x = -1 
            self.orient = ' O ' 
            self.pas_x = 0 #nul
            
        if orient_preced == ' E ':
            self.pas_y = -1 
            self.orient = ' N '         
            self.pas_x = 0 #nul 
            
        if orient_preced == ' O ':
            self.pas_y = 1 
            self.orient = ' S ' 
            self.pas_x = 0 #nul 
            
        if orient_preced == ' S ':
            self.pas_x = 1 
            self.orient = ' E ' 
            self.pas_y = 0 #nul 

        print("tourner gauche")
        
    
    def tourner_droite(self):
         
        orient_preced = self.orient
        
        if orient_preced == ' N ':
            self.pas_x = 1
            self.orient = ' E ' 
            self.pas_y = 0  #nul
            
        if orient_preced == ' E ':
            self.pas_y = 1 
            self.orient = ' S '         
            self.pas_x = 0  #nul
        
        if orient_preced == ' S ':
            self.pas_x = -1 
            self.orient = ' O '
            self.pas_y = 0  #nul
            
        if orient_preced == ' O ':
            self.pas_y = -1 
            self.orient = ' N ' 
            self.pas_x = 0  #nul
        
        print("tourner à droite")
                    
        
    def avancer(self):
            
        self.axe_hor = self.axe_hor  + self.pas_x
        self.axe_vert = self.axe_vert + self.pas_y
        
        print("Avancer")



    def prendre(self):
        """
        fonction qui va decrementer par le nombre du tresor existant dans la position, si bien sur 
        l aventurier se retrouve sur les coordoonées du trésor
        """
        pass


class Tresor(Carte):
    
    def __init__(self):
        pass    
        #coordoonées_tresor = 
         
         


if __name__ == "__main__":
    tres = Tresor()
    print("main")            