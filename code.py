#python 


class Cuprins:
    def __init__(self):
        print ("Welcome Cuprins")

class Autor:
    def __init__(self, nume):
        self.sNume = nume
        print ("Welcome Autor!")

    def nume(self):
        return self.sNume

class Carte:
    def __init__(self, titlu):
        self.sTitlu = titlu
        self.cAutor = None
        self.capitol = Capitol()
        self.subcapitol = Subcapitol()
        self.text = Text()
        self.imagine = Imagine()
        self.tabel = Tabel()
        print("Welcome Carte!")
    
    def titlu(self):
        return self.sTitlu

    def addAutor(self, autor):
        self.cAutor = autor
        return 0

    def createCapitol(self, capitol):
        self.capitol.setTitlu(capitol)
        return 0

class Capitol:
    def __init__(self):
        self.sTitlu = None
        print ("Welcome Capitol!")

    def titlu(self):
        return self.sTitlu
    
    def setTitlu(self, titlu):
        self.sTitlu = titlu
        return 0

class Subcapitol:
    def __init__(self):
        print ("Welcome Subcapitol!")

    def titlu(self):
        return ""

class Text:
    def __init__(self):
        print ("Welcome Text!")

    def text(self):
        return ""

class Imagine:
    def __init__(self):
        print ("Welcome Imagine!")

    def numeImagine(self):
        return ""

class Tabel:
    def __init__(self):
        print ("Welcome Tabel!")

    def numeTabel(self):
        return ""



c = Carte("Disco Titanic")
c.addAutor(Autor("Gelu Cristian"))
c.createCapitol("Mancare")