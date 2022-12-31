
import copy 
#from Tresor import Tresor

class Aventurier() :
    

    def __init__(self, nom, axe_hor, axe_vert, orient, chemin, tresor, montagne):
        self.nom = nom
        self.orient = orient
        self.axe_hor = axe_hor
        self.axe_vert = axe_vert
        self.chemin = chemin
        self.chemin_for_while = copy.copy(self.chemin)
        
        self.coordonne_montagne = montagne
        self.coordonne_tresor = tresor
        
        #self.carte = carte
        #
        self.pas_x = 0
        self.pas_y = 0
        
        # Nb tresor collecter
        self.Nb_tresor_col = 0
    
    def actual_pos(self):
        return self.axe_hor, self.axe_vert
    
    
    
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
        
        self.orient = self.orient
        #print("orientation")    
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
        
        self.chemin_for_while.pop(0)
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
            
        self.chemin_for_while.pop(0)
        print("tourner à droite")
        
        
        
                    
        
    def avancer(self):
        
        self.orientation()
        
        check_x = self.axe_hor  +  self.pas_x
        check_y = self.axe_vert +  self.pas_y 
        
        check = [check_x, check_y]
        
        if check in self.coordonne_montagne:
            print("rencontre d'un obstacle")
            res = 0
        
        else:
            self.axe_hor = self.axe_hor  + self.pas_x
            self.axe_vert = self.axe_vert + self.pas_y  
            print("Avancer")  
            print("position", (self.axe_hor, self.axe_vert ))      
            res = 1
        return res
        #self.pas_x = 0
        #self.pas_y = 0
    
        #return orientation(self)
        
        self.chemin_for_while.pop(0)

    def prendre(self):
        """
        fonction qui va decrementer par le nombre du tresor existant dans la position, si bien sur 
        l aventurier se retrouve sur les coordoonées du trésor
        """
        self.Nb_tresor_col = self.Nb_tresor_col +1
        
        
    def continuer(self):
        
        """
        cas d'obstacle continuer le chemin
        """
        
        pass
    
    def chasser(self):
        coordonne_tresors = list()
        for coordonee_tresor in self.coordonne_tresor:
            axe_tres_x = coordonee_tresor[0]
            axe_tres_y = coordonee_tresor[1]
            coordonne_tresors.append([axe_tres_x, axe_tres_y])
        
        for pas_chemin in self.chemin:
            if pas_chemin == 'A':
                resultat = self.avancer()
                
                # condition trésor, il prendra pas défaut 1 trésor
                if resultat == 1:
                    check_tres = [self.axe_hor, self.axe_vert]
                    if check_tres in coordonne_tresors:
                        self.prendre()
                        print("prise")
  
                
            if pas_chemin == 'G':
                self.tourner_gauche()
            
            if pas_chemin == 'D':
                self.tourner_droite()            