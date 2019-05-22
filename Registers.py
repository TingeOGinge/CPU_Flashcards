class Register:
    def __init__(self, acronym, name, description):
        self.acronym = acronym
        self.name = name
        self.description = description
    
    def getAcronym(self):
        return self.acronym
        
    def getName(self):
        return self.name
        
    def getDescription(self):
        return self.description
        
    
    