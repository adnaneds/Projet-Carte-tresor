

class Carte:
    
    def __init__(self, carte):
        
        
        self.carte = carte
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
        
    def erase(self, ancien_axe_hor, ancien_axe_vert):
        self.carte[ancien_axe_hor, ancien_axe_vert] = "."
        return self.carte



    def update_carte(self, axe_hor, axe_vert, valeur):
            
        self.carte[axe_hor, axe_vert] = valeur
        
        return self.carte            

    def __repr__(self):
        return f" le statut de la carte est le suivant : \n {self.carte}"